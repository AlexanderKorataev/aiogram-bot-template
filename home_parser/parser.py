import os
import requests
from bs4 import BeautifulSoup


class MyHomeParser:
    _headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'}

    def __init__(self, url: str):
        self.request = requests.get(url=url, headers=self._headers)
        self.status = self.request.status_code
        self.soup = BeautifulSoup(self.request.text, 'lxml')
        self.cards = []
        self.homes_url = []
        self.homes_images = []
        self.old_url = os.environ.get('HOMES_URL', '').split(',')

    def get_cards(self):
        all_cards = self.soup.select('div[class="statement-card"]')
        self.cards.extend(all_cards)

    def get_homes_url_and_images(self):
        for card in self.cards:
            card_href = card.find('a').get('href')[:37]
            if card_href not in self.old_url:
                self.homes_url.append(card_href)
                image_url = card.select('card-img')[0].find('img').get('src')
                self.homes_images.append(image_url)

    def save_to_env(self):
        os.environ['HOMES_URL'] = ','.join(self.homes_url)

    def __del__(self):
        self.request.close()
        del self