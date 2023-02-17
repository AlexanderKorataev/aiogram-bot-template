import asyncio

from messages import MESSAGES
from home_parser import MyHomeParser
from aiogram.dispatcher import Dispatcher
import os
import logging
from io import BytesIO
import requests

logging.basicConfig(level=logging.INFO)

async def check_new_houses(dp:Dispatcher, sleep_time: int):
    while True:
        await asyncio.sleep(sleep_time)
        url = os.environ.get('URL')
        if not url:
            continue
        p = MyHomeParser(url)
        if p.status == 200:
            print(f'status code: {p.status}')
        else:
            print(f'Oh shit... We have a problem, status code: {p.status}')
            continue
        p.get_cards()
        p.get_homes_url_and_images()
        if len(p.homes_url):
            p.save_to_env()
        else:
            continue
        for i, url in enumerate(p.homes_url):
            msg = f"{MESSAGES['house_is_found']}\n\n"
            image_url = p.homes_images[i]
            # Download the image and send it
            response = requests.get(image_url)
            image_bytes = BytesIO(response.content)
            await dp.bot.send_photo(os.environ['USER_ID'], photo=image_bytes, caption=msg)