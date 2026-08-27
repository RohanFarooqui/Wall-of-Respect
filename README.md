# Wall of Respect

Wall of Respect is an internship project developed at TouchStone. It provides a public recognition page and an administration interface for managing associates, campaigns, users, roles, and role permissions.

The visual concept was inspired by [Character Select](https://www.characterselect.com/talent).

## Technology

- Flask REST API
- Embedded SQLite database
- Django web interface
- HTML, CSS, JavaScript, and Bootstrap

SQLite is included with Python, so MySQL Server or MySQL Workbench is not required.

## Requirements

- Python 3.10 recommended
- Windows for the included batch launchers

## Installation

Open PowerShell in the project root and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the complete project

```powershell
.\Run.bat
```

This starts:

- Flask API: <http://127.0.0.1:5000>
- Django interface: <http://127.0.0.1:8000>

Keep the API window open while using the interface.

## Run components manually

Use two terminals from the project root.

Terminal 1 — API:

```powershell
python API\app.py
```

Terminal 2 — interface:

```powershell
python Interface\manage.py runserver 127.0.0.1:8000
```

## Initial database setup

The API uses `API/wall_of_respect.db`. When this file does not exist, startup creates the SQLite schema and safely imports the historical records from `API/database/seed.sql`.

Initialization is transactional and versioned. If startup is interrupted, incomplete seed changes are rolled back and initialization can run again safely.

To use a different SQLite location, set `WOR_DB_PATH` before starting the API:

```powershell
$env:WOR_DB_PATH = "C:\path\to\wall_of_respect.db"
python API\app.py
```

## Demo login

- Username: `admin`
- Password: `1234`

These credentials are intended only for local demonstration. Change them before using the project in another environment.

## Media storage

Uploaded images are owned and served by the Flask API:

- Associate images: `API/media/associates/`
- User images: `API/media/users/`
- Public URLs: `http://127.0.0.1:5000/media/...`

SQLite stores only each image path, not the image binary. The Django interface sends new uploads to the API.

## Project structure

```text
Wall-of-Respect/
├── API/
│   ├── api/                 # Flask request handlers and media handling
│   ├── database/            # SQLite connection, repositories, and seed data
│   ├── media/               # Associate and user images
│   ├── app.py               # Flask routes and API entry point
│   └── wall_of_respect.db   # Generated local SQLite database
├── Interface/
│   ├── INTERFACE/           # Django project code
│   ├── static/              # CSS, JavaScript, fonts, and interface images
│   ├── templates/           # Django HTML templates
│   ├── manage.py            # Django command entry point
│   └── db.sqlite3           # Django session database
├── requirements.txt         # Python dependencies for API and interface
└── Run.bat                  # Starts both components
```

## Main API routes

- `GET /` — API and database status
- `POST /v1/login` — user login
- `GET|POST /v1/user` — user operations
- `GET|POST /v1/role` — role operations
- `GET|POST /v1/associate` — associate operations
- `GET|POST /v1/campaign` — campaign operations
- `POST /v1/media` — image upload
- `GET /media/<path>` — image delivery

## Notes

- Start the API before opening pages that load data from it.
- `API/wall_of_respect.db`, virtual environments, and Python cache files are excluded by `.gitignore`.
- The project is configured for local development and demonstration, not production deployment.