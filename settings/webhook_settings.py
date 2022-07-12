"""Settings required to run the webhook"""
import os

from .bot_settings import TOKEN

# Application name
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# Webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# Webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

# Сhecking for the existence of a variable
if (not HEROKU_APP_NAME 
    or not WEBAPP_PORT):
    exit()