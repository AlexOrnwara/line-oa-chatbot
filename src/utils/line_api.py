import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the LINE channel access token from environment variables
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")


def send_message(user_id, message):
    """Send a message to a user via LINE Messaging API."""
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
    }
    payload = {"to": user_id, "messages": [{"type": "text", "text": message}]}

    response = requests.post(url, headers=headers, json=payload)
    return response.status_code, response.json()
