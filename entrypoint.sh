#!/bin/sh
cd src
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

# running with guicorn
cd src
gunicorn djangosetup.wsgi:application --bind 0.0.0.0:8000
