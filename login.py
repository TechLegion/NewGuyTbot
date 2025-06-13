import configparser
from telethon import TelegramClient, events, Button
import asyncio
import random
from datetime import datetime
from dotenv import load_dotenv
import os
from aiohttp import web

# Load environment variables
load_dotenv()

# Get credentials from environment variables
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE_NUMBER')

# Create the client and connect using the pre-generated session
client = TelegramClient('my_session', api_id, api_hash)

CHANNEL = 2361324101  # Channel ID for VIP channel
BUTTON_TEXT = '🎯 TrojanBot'        # Button to click
DELAY_RANGE = (10, 30)          # Random delay in seconds

# Create web application
app = web.Application()

async def health_check(request):
    return web.Response(text="OK", status=200)

app.router.add_get('/', health_check)

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
                        # Extract contract key from message
                        contract_key = None
                        for line in event.text.split('\n'):
                            if 'Contract:' in line:
                                contract_key = line.split('Contract:', 1)[1].strip()
                                break
                        if contract_key:
                            await client.send_message('solana_trojanbot', contract_key)
                            print(f"[{now}] [INFO] Sent contract key to @solana_trojanbot: {contract_key}")
                        else:
                            print(f"[{now}] [WARN] No contract key found in message!")
                    except Exception as e:
                        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(f"[{now}] [ERROR] Failed to click button or start bot: {e}")
                    return
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] [INFO] No 'TrojanBot' button found in this message.")

async def main():
    # Start the client without phone number (using session file)
    await client.connect()
    if not await client.is_user_authorized():
        print("Session file not found or invalid. Please run generate_session.py first.")
        return
    
    print('Logged in successfully! Listening for new messages...')
    
    # Start the web server
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', 8080)))
    await site.start()
    print(f'Health check server started on port {os.environ.get("PORT", 8080)}')
    
    # Keep the bot running
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())