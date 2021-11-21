from telethon import TelegramClient
import logging
import time
import os

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


Var = os.environ.get

APP_ID= (Var("API_ID"))
API_HASH = Var("API_HASH")
TOKEN = Var("TOKEN")

#lel




tbot = TelegramClient('botto', APP_ID, API_HASH).start(bot_token=TOKEN)
