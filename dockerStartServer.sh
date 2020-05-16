#!/bin/bash

# Start Server in development or production
# Development will watch for python file changes

serverFile="${PWD}/src/server.py"
devServerFile="${PWD}/sourceChangeMonitor.py"

if [ "$APP_ENVIRONMENT" = "development" ]
then
    # watch files for changes
    python $devServerFile $serverFile
else
    # Run server file
    python $serverFile
fi