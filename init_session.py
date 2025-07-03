import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv
load_dotenv()
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE_NUMBER')

with TelegramClient('session_name', api_id, api_hash) as client:
    client.start(phone)
