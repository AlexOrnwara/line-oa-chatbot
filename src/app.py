# src/app.py
from flask import Flask, request, jsonify, render_template

from src.prisma_client import prisma
from src.utils.webhook_handler import handle_event
import asyncio

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    print("Received body:", body)

    # Check if the event is present
    if "events" in body:
        for event in body["events"]:
            asyncio.run(handle_event(event))  # Call the async function

    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(port=5000)
