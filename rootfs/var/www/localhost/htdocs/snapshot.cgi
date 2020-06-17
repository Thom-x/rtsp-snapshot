#!/bin/bash

URL="$(</tmp/url)"
timestamp=$(date +%Y-%m-%d_%H-%M-%S-%3N)
ffmpeg -y -rtsp_transport tcp -i $URL -frames:v 1 /var/www/localhost/htdocs/snapshots/snapshot_$timestamp.jpg -loglevel panic
echo "Content-type: text/html" 
echo "Status: 302"
echo "Location: snapshots/snapshot_$timestamp.jpg"
echo
