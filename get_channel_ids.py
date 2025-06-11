from telethon import TelegramClient
import configparser
import os
from dotenv import load_dotenv

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

client = TelegramClient('userbot_session', api_id, api_hash)

async def main():
    await client.start(phone=phone)
    print('Fetching your channels...')
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f"Title: {dialog.title}\nID: {dialog.entity.id}\nUsername: {getattr(dialog.entity, 'username', None)}\n---")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main()) 