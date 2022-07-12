"""Configuring commands displayed in the Telegram interface"""
from aiogram.types import BotCommand

# List of commands
commands = [
    BotCommand(command="/start", description="Bot start🚀"),
    BotCommand(command="/help", description="Help🆘"),
]