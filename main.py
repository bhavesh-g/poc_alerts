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

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Frontend connected through socket.')

def send_alert_conditionally():
    current_time_seconds = int(time.time())
    print(current_time_seconds, 'not divisible by 3')
    if current_time_seconds % 3 == 0:
        
        alert_message = f"Random Alert: {random.randint(1, 100)}"
        socketio.emit('receive_alert', {'message': alert_message}, broadcast=True)

def schedule_alert_sender():
    schedule.every(10).seconds.do(send_alert_conditionally)  # Adjust the interval as needed

if __name__ == '__main__':
    t = threading.Thread(target=schedule_alert_sender)
    t.start()
    socketio.run(app, debug=True, port=5000)
    print('stuff')
