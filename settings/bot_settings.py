"""Settings required to work with the telegram api"""
import logging
import os

# Getting a token for api telegrams from an environment variable
TOKEN = os.getenv('TOKEN')

# Сhecking for the existence of a variable
if not TOKEN:
    logging.error("not TOKEN!")
    exit()
