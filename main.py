"""Webwook entry point"""
import logging
import asyncio
import os

from settings.bot_settings import TOKEN
from settings.webhook_settings import (WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT)
from settings.bot_commands_settings import commands

from handlers import common

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from plugins import check_new_houses


logger = logging.getLogger(__name__)

# Declaring and initializing bot and dispatcher objects
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Registration of commands displayed in the Telegram interface
async def set_commands(bot: Bot):
    await bot.set_my_commands(commands)


async def on_startup(dispatcher) -> None:
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    loop = asyncio.get_event_loop()
    loop.create_task(check_new_houses(dp, int(os.getenv('TIMEOUT'))))

async def on_shutdown(dispatcher) -> None:
    await bot.delete_webhook()


def main() -> None:
    # Setting up logging
    from settings.debug_settings import LOGGING_LEVEL
logging.basicConfig(
        level=LOGGING_LEVEL,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Registration of handlers
    common.register_client_handlers(dp)

    # Installing bot commands
    set_commands(bot)
    
    # Webhook start
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )


if __name__ == '__main__':
    main()