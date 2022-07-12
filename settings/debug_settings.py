"""Settings required for logging in DEBUG mode"""
import os

# Getting the DEBUG value from an environment variable
DEBUG = os.getenv('DEBUG')

# Checking for the existence of a variable
if not DEBUG:
    exit()