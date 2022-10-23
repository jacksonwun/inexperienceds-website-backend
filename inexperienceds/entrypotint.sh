#!/bin/bash
mkdir /var/log/gunicorn
touch /var/log/gunicorn/gunicorn-error.log
touch /var/log/gunicorn/gunicorn-access.log

APP_PORT=${PORT:-8000}
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm inexperienceds.wsgi:application -w 4 -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:${APP_PORT}" --log-config log.conf --threads 4