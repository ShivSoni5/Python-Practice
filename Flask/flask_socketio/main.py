#!/usr/bin/env python

from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
#    send(msg, broadcast=True)
    if msg == "hi":
        send("hello")
    else:
        send(msg)

if __name__ == '__main__':
    socketio.run(app)
