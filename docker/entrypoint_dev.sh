#!/usr/bin/env bash

trap cleanup SIGINT SIGTERM

EXPOSE_PORT=${EXPOSE_PORT:-8000}
SLEEP_AFTER_CRASH=${SLEEP_AFTER_CRASH:-5}

cleanup () {
    echo "SIGTERM"
    kill -s SIGTERM $!
    exit 0
}

start () {
    pip-sync requirements.txt --pip-args "--src /root/src"
    python manage.py migrate --noinput

    while true; do
        cd pepposaur_project/
        python manage.py runserver 0.0.0.0:$EXPOSE_PORT
        wait $!
        sleep $SLEEP_AFTER_CRASH
    done
}

start
