import asyncio

from messages import MESSAGES
from home_parser import MyHomeParser
from aiogram.dispatcher import Dispatcher
import os
import logging

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
        p.get_homes_id()
        p.get_homes_url()
        if p.homes_url and p.homes_id:
            p.save_to_env()
        else:
            continue
        urls_str = '\n'.join(p.homes_url)
        msg = f"{MESSAGES['house_is_found']}\n\n{urls_str}"

        user_ids = os.environ.get('USER_IDS', '').split(',')
        logging.info('user_ids = ', user_ids)
        for user_id in user_ids:
            try:
                await dp.bot.send_message(user_id, msg)
            except Exception as e:
                print(e)