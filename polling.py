"""Polling entry point"""
import logging
import asyncio

from settings.bot_settings import TOKEN
from settings.bot_commands_settings import commands

from handlers import common

from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.dispatcher import Dispatcher


logger = logging.getLogger(__name__)

# Declaring and initializing bot and dispatcher objects
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Registration of commands displayed in the Telegram interface
async def set_commands(bot: Bot):
    await bot.set_my_commands(commands)


async def main() -> None:
    # Setting up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Registration of handlers
    common.register_client_handlers(dp)

    # Installing bot commands
    await set_commands(bot)

    # Polling start
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())