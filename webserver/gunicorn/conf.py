"""
File 		    : 	gunicorn.conf.py
Description     :   file holds the configuration detail for gunicorn WSGI server
Project Name    :   Airtel Portal
Created by Pankaj on 30/06/2021
Copyright (c) 2021 EverestIMS. All rights reserved.

For more detail:
https://docs.gunicorn.org/en/latest/settings.html
"""
import os


BASE_DIR = os.path.dirname(__file__)

LOG_DIR = os.getcwd() + os.sep + 'logs' + os.sep + 'gunicorn'
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

# Logging
accesslog = LOG_DIR + os.sep + 'access.log'
access_log_format = '%(t)s %(s)s [t:%(L)s] %(r)s %(l)s %(b)s'
errorlog = LOG_DIR + os.sep + 'error.log'
loglevel = 'warning'                    # 'debug'  'info' 'warning' 'error' 'critical'

# proc_name = 'airtel_portal' 
# default_proc_name = 'gunicorn'

# Set environment variables in the execution environment.
# Should be a list of strings in the key=value format.
# raw_env = [
#     "DJANGO_SETTINGS_MODULE=settings"
#     ]

pidfile = BASE_DIR + os.sep + 'gunicorn.pid'
worker_tmp_dir = BASE_DIR

# adding application/lib related python path
pythonpath = '/opt/portal/source,/opt/portalenv/lib/python2.7/site-packages'

# $ gunicorn -b 127.0.0.1:8000 -b [::1]:8000 test:app
bind = ['127.0.0.1:9000']

# The number of worker processes for handling requests.
# A positive integer generally in the 2-4 x $(NUM_CORES) range
workers = 4

# The maximum number of simultaneous clients.
worker_connections = 1000

# The maximum number of requests a worker will process before restarting.
# Any value greater than zero will limit the number of requests a worker will process before automatically restarting. 
# This is a simple method to help limit the damage of memory leaks.
# If this is set to zero (the default) then the automatic worker restarts are disabled.
max_requests = 256

# Workers silent for more than this many seconds are killed and restarted.
timeout = 30

# The number of seconds to wait for requests on a Keep-Alive connection.
# Generally set in the 1-5 seconds range for servers with direct connection to the client 
# (when you don't have separate load balancer). When Gunicorn is deployed behind a load balancer, 
# it often makes sense to set this to a higher value.
keepalive = 10

