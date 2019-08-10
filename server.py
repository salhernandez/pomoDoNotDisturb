import flask
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = flask.Flask(__name__)
socketio = SocketIO(app)

# sites
@app.route('/hub')
def hub():
    data = open('hub.html').read()
    return data

@app.route('/status')
def status():
    data = open('status.html').read()
    return data

# libraries
@app.route('/getSocketIO')
def getSocketIO():
    data = open('socket.io.js').read()
    return data

# set statuses
@socketio.on('setRed')
def setRed():
    print("bruh")
    emit('setRed', broadcast=True)

@socketio.on('setGreen')
def setGreen():
    emit('setGreen', broadcast=True)

@socketio.on('setBlue')
def setBlue():
    emit('setBlue', broadcast=True)

# connection status
@socketio.on('connect')
def on_connect():
    print ("%s USER CONNECTED " %  flask.request.sid)

@socketio.on('disconnect')
def on_disconnect():
    print ("%s USER DISCONNECTED " %  flask.request.sid)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
