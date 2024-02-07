from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')  # Set cors_allowed_origins to '*' for development; restrict in production

@app.route('/')
def index():
    return '<html><body><h1>Welcome to the Alert App!</h1><a href="/create_alert">Create Dummy Alert</a></body></html>'

@app.route('/create_alert', methods=['GET'])
def create_alert():
    alert_message = f"Dummy Alert: {random.randint(1, 100)}"
    try:
        socketio.emit('receive_alert', {'message': alert_message})
    except Excwption as e:
        print(e)
    return f'<html><body><h1>{alert_message}</h1><a href="/">Back to Home</a></body></html>'

@socketio.on('connect')
def handle_connect():
    print('Frontend connected through socket.')

if __name__ == '__main__':

    try:
        socketio.run(app, debug=True, port=5000)
    except Exception as e:
        print(e,'2')
