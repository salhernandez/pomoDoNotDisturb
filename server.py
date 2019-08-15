from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# sites
@app.route('/hub')
def hub():
    # data = open('hub.html').read()
    # return data
    return render_template('hub.html')

@app.route('/status')
def status():
    return render_template('status.html')

# set statuses
@socketio.on('setRed')
def setRed():
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
    print ("%s USER CONNECTED " % request.sid)

@socketio.on('disconnect')
def on_disconnect():
    print ("%s USER DISCONNECTED " % request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
