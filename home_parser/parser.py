import os
import pandas as pd
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
        self.homes_id = []
        
        homes_df = pd.DataFrame({
            'url': os.environ.get('HOMES_URL', '').split(','),
            'id': os.environ.get('HOMES_ID', '').split(',')
        })
        self.homes_df = homes_df.drop_duplicates()

    def get_cards(self):
        all_cards = self.soup.select('div[class="statement-card"]')
        self.cards.extend(all_cards)

    def get_homes_url(self):
        old_urls = self.homes_df['url'].tolist()
        for card in self.cards:
            card_href = card.find('a').get('href')[:37]
            if card_href not in old_urls:
                self.homes_url.append(card_href)

    def get_homes_id(self):
        old_ids = self.homes_df['id'].tolist()
        for card in self.cards:
            home_id = int(card.get('data-product-id'))
            if home_id not in old_ids:
                self.homes_id.append(home_id)

    def save_to_env(self):
        homes_df = pd.DataFrame({
            'url': self.homes_url,
            'id': self.homes_id
        })
        homes_df = pd.concat([self.homes_df, homes_df])
        homes_df = homes_df.drop_duplicates()
        homes_url = ','.join(homes_df['url'].tolist())
        homes_id = ','.join([str(i) for i in homes_df['id'].tolist()])
        os.environ['HOMES_URL'] = homes_url
        os.environ['HOMES_ID'] = homes_id

    def __del__(self):
        self.request.close()
        del self