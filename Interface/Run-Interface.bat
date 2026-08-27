@echo off
cd /d "%~dp0"
python manage.py runserver 127.0.0.1:8000
