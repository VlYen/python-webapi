# Python Web API

A FastAPI REST API for managing **students** and **school classes**. It uses a layered design (routers → services → repositories) and stores data in SQLite or SQL Server.

## Features

- CRUD endpoints for students and school classes
- Health check endpoint
- Pydantic models with camelCase JSON fields
- Repository pattern with a pluggable repository factory
- Database connection factory for SQLite (`sqlite3`) or SQL Server (`pyodbc`)
- File logging to `app.log` with a per-request correlation ID
- CORS enabled for all origins
- Interactive API docs (Swagger UI) at `/docs`

## Tech stack

- Python 3.13
- [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/)
- Pydantic / pydantic-settings
- SQLite / SQL Server (ODBC Driver 18)
- python-dotenv

## Project structure

```text
python-webapi/
├── requirements.txt
├── .env                      # Local environment settings (not committed)
├── __docs/                   # Developer notes
└── src/
    ├── main.py               # FastAPI app entry point
    ├── app_logging/          # Logging setup, filter, and correlation-ID middleware
    ├── common/               # Settings, pretty JSON response, utilities
    ├── factories/            # Connection factory and repository factory/registry
    ├── models/               # Pydantic models
    ├── repositories/         # Data access (SQLite implementations)
    ├── routers/              # API endpoints (health, students, classes)
    └── services/             # Business logic and SQLite table setup script
```

## Getting started

### 1. Create and activate a virtual environment

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

On macOS/Linux:

```sh
python -m venv myenv
source myenv/bin/activate
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

To use SQL Server, also install [Microsoft ODBC Driver 18 for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server).

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
APP_NAME=Python Web API
APP_DESCRIPTION=Students and classes API
VERSION=1.0.0

# Database: "sqlite" or "sqlserver"
DB_TYPE=sqlite
SQLITE_DB_PATH=mydatabase.db

# Required only when DB_TYPE=sqlserver
DB_SERVER=localhost
DB_DATABASE=your_database
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

| Variable | Description |
| --- | --- |
| `APP_NAME` | API title shown in the docs and health response |
| `APP_DESCRIPTION` | API description shown in the docs |
| `VERSION` | API version |
| `DB_TYPE` | `sqlite` or `sqlserver` (required) |
| `SQLITE_DB_PATH` | SQLite file path, relative to the working directory |
| `DB_SERVER`, `DB_DATABASE`, `DB_USERNAME`, `DB_PASSWORD` | SQL Server connection settings |

> Do not commit `.env`. It is already listed in `.gitignore`.

### 4. Create the SQLite tables

Run from the `src` folder so the database is created where the app looks for it:

```sh
cd src
python services/sqlite_table_creator.py
```

This creates the `Students`, `SchoolClasses`, `Vendors`, and `Products` tables if they do not exist.

### 5. Run the API

Run from the `src` folder (the app uses imports relative to `src`):

```sh
cd src
uvicorn main:app --reload
```

To use a different port:

```sh
uvicorn main:app --port 8111
```

Then open:

- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## API endpoints

### Health

| Method | Path | Description |
| --- | --- | --- |
| GET | `/health` | Returns app name, version, and current time |

### Students

| Method | Path | Description |
| --- | --- | --- |
| GET | `/students` | List all students |
| GET | `/students/{student_id}` | Get a student by ID |
| POST | `/students` | Create a student |
| PUT | `/students` | Update a student (ID in body) |
| DELETE | `/students/{student_id}` | Delete a student |

Example body:

```json
{
  "firstName": "Jane",
  "lastName": "Doe",
  "ssn": "123-45-6789"
}
```

### Classes

| Method | Path | Description |
| --- | --- | --- |
| GET | `/classes` | List all classes |
| GET | `/classes/{id}` | Get a class by ID |
| POST | `/classes` | Create a class |
| PUT | `/classes` | Update a class (ID in body) |
| DELETE | `/classes/{class_id}` | Delete a class |

Example body:

```json
{
  "className": "Intro to Python",
  "description": "Python basics",
  "instructor": "John Smith",
  "startDate": "2026-01-10",
  "endDate": "2026-05-20",
  "capacity": 25,
  "isActive": 1
}
```

## Logging

Logs are written to `app.log` in the working directory. Each request gets a correlation ID, taken from the `X-Custom-Value` request header or generated as a UUID.

## Architecture

```text
Router (routers/) → Service (services/) → Repository (repositories/) → Database
                                              ↑
                     RepositoryFactory + ConnectionFactory (factories/)
```

- `ConnectionFactory` returns a SQLite or SQL Server connection based on `DB_TYPE`.
- `repository_registry.get_repository_factory()` registers a repository for each model.
- Services get their repositories from the factory, so data access can be swapped without changing routers.

> The registered repositories currently use SQLite SQL. Use `DB_TYPE=sqlite` unless SQL Server repositories are added.

## Docker

```sh
docker build -t simple-python-webapp .
docker run --rm -it -p 8081:8000 simple-python-webapp:latest
```

> A `Dockerfile` is not in the repository yet. Add one before running these commands.

## Developer notes

More notes are in [`__docs/`](./__docs), including virtual environment, FastAPI, logging, database, Docker, and Git notes.
