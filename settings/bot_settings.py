"""Settings required to work with the telegram api"""
import os

# Getting a token for api telegrams from an environment variable
# TOKEN = os.getenv('TOKEN')
TOKEN = '5408763692:AAEtPK-CXZtmvliE6-cpviepnr3FnW3HJlw'

# Сhecking for the existence of a variable
if not TOKEN:
    exit()