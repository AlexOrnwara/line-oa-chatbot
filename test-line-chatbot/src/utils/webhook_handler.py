from src.utils.line_api import send_message


def handle_event(event):
    """Handle the follow event and send a welcome message."""
    user_id = event['source']['userId']
    print(f'User ID: {user_id}')  # Print the user ID

    # Send a welcome message to the user
    status_code, response = send_message(user_id, "Thank you for following us!")
    print(f'Message sent status: {status_code}, Response: {response}')
