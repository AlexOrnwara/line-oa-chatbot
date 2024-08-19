# src/utils/webhook_handler.py
from src.utils.line_api import send_message
from prisma_client import create_user  # Import the create_user function


async def handle_event(event):
    """Handle incoming events and respond accordingly."""
    if event["type"] == "message":
        user_id = event["source"]["userId"]
        print(f"User ID: {user_id}")  # Print the user ID

        # Store the user_id in the database
        await create_user(user_id)

        # Send a welcome message to the user
        status_code, response = send_message(user_id, "Thank you for following us!")
        print(f"Message sent status: {status_code}, Response: {response}")
    else:
        print(f'Unhandled event type: {event["type"]}')
