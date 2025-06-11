from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get credentials from environment variables
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE_NUMBER')

print("Starting session generation...")
print(f"Using phone number: {phone}")

# Create the client
client = TelegramClient('my_session', api_id, api_hash)

# Start the client
client.start()

print("\nSession file generated successfully!")
print("You can find the session file as 'my_session.session'")
print("\nNext steps:")
print("1. Upload 'my_session.session' to Railway/Render through their web dashboard")
print("2. Deploy your bot - it will use this session file automatically")
print("3. DO NOT commit the session file to GitHub")

# Disconnect the client
client.disconnect() 