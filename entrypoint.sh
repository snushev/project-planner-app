#!/bin/bash

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000
