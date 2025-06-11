# Telegram Bot

This is a Telegram bot that monitors a specific channel and automatically interacts with messages containing a specific button.

## Deployment on Render

1. Create a new account on [Render](https://render.com) if you haven't already
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure the following environment variables in Render's dashboard:
   - `API_ID`: Your Telegram API ID
   - `API_HASH`: Your Telegram API Hash
   - `PHONE_NUMBER`: Your phone number in international format (e.g., +1234567890)

## Local Development

1. Create a `.env` file with the following variables:
   ```
   API_ID=your_api_id
   API_HASH=your_api_hash
   PHONE_NUMBER=your_phone_number
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the bot:
   ```bash
   python login.py
   ``` 