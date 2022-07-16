#!/bin/bash

URL="$(</tmp/url)"
timestamp=$(date +%Y-%m-%d_%H-%M-%S-%3N)
ffmpeg -y -rtsp_transport tcp -i $URL -frames:v 1 /var/www/localhost/htdocs/snapshots/snapshot_$timestamp.jpg -loglevel panic
echo -e "Content-type: text/html\r" 
echo -e "Status: 302\r"
echo -e "Location: snapshots/snapshot_$timestamp.jpg\r"
echo -e "\r"
