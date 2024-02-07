from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import time
import random
import schedule
import threading

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')  # Set cors_allowed_origins to '*' for development; restrict in production


def send_alert_conditionally():
    current_time_seconds = int(time.time())
    print(current_time_seconds, 'not divisible by 3')
    if current_time_seconds % 3 == 0:
        
        alert_message = f"Random Alert: {random.randint(1, 100)}"
        socketio.emit('receive_alert', {'message': alert_message}, broadcast=True)


if __name__ == '__main__':
    print('mainnn')
    socketio.run(app, debug=True, port=5000)
    print('stuff')
    while True:
        send_alert_conditionally()
