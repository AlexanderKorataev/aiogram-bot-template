"""Configuring commands displayed in the Telegram interface"""
from aiogram.types import BotCommand

# List of commands
commands = [
    BotCommand(command="/start", description="Bot start🚀"),
    BotCommand(command="/help", description="Help🆘"),
    BotCommand(command='set_link', description='установить новую ссылку для поиска'),
    BotCommand(command='cancel', description='отменить действие')
]