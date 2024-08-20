# src/utils/webhook_handler.py
from src.utils.line_api import send_message
from src.prisma_client import create_user, prisma, query_db, clear_all_data  # Import the create_user function


async def handle_event(event):
    """Handle incoming events and respond accordingly."""
    if event['type'] == 'follow':
        user_id = event['source']['userId']
        print(f'User ID: {user_id}')  # Print the user ID

        # Validate user_id format
        if not isinstance(user_id, str) or len(user_id) == 0:
            print("Invalid user_id format.")
            return

        # Store the user_id in the database
        # await create_user(user_id)
        # await query_db()
        await clear_all_data()

        # Send a welcome message to the user
        status_code, response = send_message(user_id, "Thank you for following us!")
        print(f'Message sent status: {status_code}, Response: {response}')
