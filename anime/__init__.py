from telethon import TelegramClient
import logging
import time
import os

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)




APP_ID= os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)

#lel




tbot = TelegramClient('botto', APP_ID, API_HASH).start(bot_token=TOKEN)
