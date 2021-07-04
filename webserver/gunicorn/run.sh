#!/bin/sh


source /opt/portalenv/bin/activate

start()
{
/opt/portalenv/bin/gunicorn --config webserver/gunicorn/conf.py username.wsgi:application
}
start

