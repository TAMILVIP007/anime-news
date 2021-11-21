from telethon import TelegramClient
from config import *
import logging
import time
import os

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


Var = os.environ.get

API_KEY= (Var("API_KEY"))
API_HASH = Var("API_HASH")
TOKEN = Var("TOKEN")

#lel




tbot = TelegramClient('botto', API_KEY, API_HASH).start(bot_token=TOKEN)
