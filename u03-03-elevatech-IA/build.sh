#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py seed

# cria superusuário se ainda não existir (usa env vars DJANGO_SUPERUSER_*)
python manage.py createsuperuser --noinput 2>/dev/null || true