import configparser
from telethon import TelegramClient, events, Button
import asyncio
import random
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read credentials from Keys.txt
config = configparser.ConfigParser()
config.read_dict({'DEFAULT': {}})
with open('Keys.txt', 'r') as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            config['DEFAULT'][key.strip()] = value.strip()

api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE_NUMBER')

# Create the client and connect
client = TelegramClient('userbot_session', api_id, api_hash)

CHANNEL = 'BullishCallsPremium'  # Channel username without @
BUTTON_TEXT = '🎯 TrojanBot'        # Button to click
DELAY_RANGE = (10, 60)          # Random delay in seconds

@client.on(events.NewMessage(chats=CHANNEL))
async def handler(event):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] New message received.")
    print(f"[{now}] Message text: {event.text}")
    # Check if the message has buttons
    if event.buttons:
        for row in event.buttons:
            for button in row:
                print(f"Button text: '{getattr(button, 'text', None)}'")
                if getattr(button, 'text', '').strip() == BUTTON_TEXT:
                    delay = random.randint(*DELAY_RANGE)
                    print(f"[{now}] [INFO] 'TrojanBot' button found. Clicking in {delay} seconds...")
                    await asyncio.sleep(delay)
                    try:
                        await event.click(text=BUTTON_TEXT)
                        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f"[{now}] [INFO] Clicked 'TrojanBot' button!")
                    except Exception as e:
                        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f"[{now}] [ERROR] Failed to click button: {e}")
                    return
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] [INFO] No 'TrojanBot' button found in this message.")

async def main():
    await client.start(phone=phone)
    print('Logged in successfully! Listening for new messages...')
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())