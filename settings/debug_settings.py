"""Settings required for logging in DEBUG mode"""
import logging
import os

# Getting the DEBUG value from an environment variable
DEBUG = os.getenv('DEBUG')
if DEBUG:
    LOGGING_LEVEL = logging.DEBUG
else:
    LOGGING_LEVEL = logging.INFO

# Checking for the existence of a variable
if not DEBUG:
    logging.error("not DEBUG!")
    exit()