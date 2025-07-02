from fastapi import FastAPI
from telethon import TelegramClient, events
import asyncio
import os

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

KEYWORDS = ['internship', 'hiring', 'job', 'opening']

TARGET_GROUP_TITLES = [
    'Engineering 2026 batch',
    'Placement Announcements',
    'Internship Offers 2025',
    'test'
]

app = FastAPI()

client = TelegramClient('session_name', api_id, api_hash)

@app.on_event("startup")
async def startup_event():
    print("Starting bot...")
    await client.start()

    groups = []
    async for dialog in client.iter_dialogs():
        if dialog.is_group and dialog.title in TARGET_GROUP_TITLES:
            groups.append(dialog.entity)

    if not groups:
        print("No target groups found!")
        return

    print(f"Listening to groups: {[g.title for g in groups]}")

    @client.on(events.NewMessage(chats=groups))
    async def handler(event):
        if event.message.text:
            text = event.message.text.lower()
            if any(keyword in text for keyword in KEYWORDS):
                print(f"\n[Filtered] From {event.chat.title}: {event.message.text}")
                with open('filtered_msgs.txt', 'a', encoding='utf-8') as f:
                    f.write(f"[{event.chat.title}] {event.message.text}\n")
                await client.forward_messages('offers', event.message)

    asyncio.create_task(client.run_until_disconnected())

@app.get("/")
async def root():
    return {"message": "Placement bot is running!"}
