@echo off
cd /d "%~dp0"

start "Wall of Respect API" python API\app.py
python Interface\manage.py runserver 127.0.0.1:8000
