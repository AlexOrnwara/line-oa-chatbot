# app.py
from flask import Flask, request, jsonify
from src.utils.webhook_handler import handle_event

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.get_json()
    print("Received body:", body)

    # Check if the event is a follow event
    if 'events' in body:
        for event in body['events']:
            if event['type'] == 'follow':
                handle_event(event)  # Call the function to handle the follow event

    return jsonify(status='ok')


if __name__ == '__main__':
    app.run(port=5000)
