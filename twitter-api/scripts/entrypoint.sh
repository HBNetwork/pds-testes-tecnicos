#!/bin/bash

set -e

python manage.py wait_for_db
python manage.py migrate
python manage.py loaddata data/db.json

gunicorn --capture-output \
  --access-logfile '-' \
  --error-logfile '-' \
  main.wsgi:application --bind 0.0.0.0:8000
