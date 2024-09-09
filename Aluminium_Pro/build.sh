#!/bin/bash

# Build the Project
echo "Building the project"


# Install Python dependencies
pip install -r requirements.txt

# Optional: Run migrations (if needed)
echo "Running migrations"
python manage.pu makemigrations --noinput
python manage.py migrate --noinput


# Run Django collectstatic command to gather static files
echo "Collecting static files"
python manage.py collectstatic --noinput


