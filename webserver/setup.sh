#!/bin/sh

#
#   Gunicorn installation
#       - application environment as pip package
#
#   Nginx installation
#       - os level as 
#


cd /etc/systemd/system
# Setting link for gunicorn server
sudo ln -s /opt/testportal_ts/source/webserver/gunicorn/gunicorn.service
# setting link for ngnx server
sudo ln -s /opt/testportal_ts/source/webserver/nginx/nginx.service


systemctl daemon-reload