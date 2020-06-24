#!/bin/sh

python manage.py wait_for_db
python manage.py migrate
python manage.py collectstatic
gunicorn system.wsgi:application --bind 0.0.0.0:8000
