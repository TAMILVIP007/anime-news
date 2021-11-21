import requests 
from .. import tbot
from telethon import Button, events


@tbot.on(events.NewMessage(pattern="[/!]anime"))
async def _(e):
   f = requests.get('https://anime-news-api-production-5b50.up.railway.app/').json()
   y = f['image']
   z = f['post_url']
   lol = f['title']
   ok = f['info']
   msg = (f'**Title:**\n{lol}\n\n')
   msg += (f'**Info:**\n{ok}\n')
   await e.respond(msg, file=y, buttons=Button.url('Click', f'{z}'))
