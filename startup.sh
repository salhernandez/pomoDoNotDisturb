#!/bin/bash
chromium-browser --disable-session-crashed-bubble --disable-infobars http://0.0.0.0:5000/hub
sudo python3 /home/pi/Desktop/pomoDoNotDisturb/server.py