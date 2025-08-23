#!/bin/sh
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Load initial data
echo "Loading initial data..."
python manage.py loaddata initial_data.json

# Start the Gunicorn server
echo "Starting Gunicorn server..."
gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000