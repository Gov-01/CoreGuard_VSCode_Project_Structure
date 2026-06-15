
CoreGuard — Incident / Risk Events Viewer
=========================================

This repository contains a small full‑stack example: a FastAPI backend (SQLite) and a React + Vite frontend. The project provides event listing, details, notes, assignment and a simple audit trail.

**Quick Overview**
- **Backend:** FastAPI application in backend/app providing REST endpoints for events, notes, assignment, and summary.
- **Frontend:** React + Vite app in frontend/ that consumes the backend API and renders a dashboard and event detail pages.

**Repository Layout**
- **Backend:** [backend/app](backend/app)
	- **Main app:** [backend/app/main.py](backend/app/main.py)
	- **Models:** [backend/app/models.py](backend/app/models.py)
	- **Schemas:** [backend/app/schemas.py](backend/app/schemas.py)
	- **Database config:** [backend/app/database.py](backend/app/database.py)
	- **Routes:** [backend/app/routes](backend/app/routes) (several route files are present; some are currently empty stubs)
	- **Services:** [backend/app/services](backend/app/services) (service modules exist; several are currently empty stubs)
	- **Tests:** [backend/tests](backend/tests) (test files are present but many are empty)

- **Frontend:** [frontend/src](frontend/src)
	- **Entry:** [frontend/src/main.tsx](frontend/src/main.tsx)
	- **Router / App:** [frontend/src/App.tsx](frontend/src/App.tsx)
	- **API client:** [frontend/src/api/eventApi.ts](frontend/src/api/eventApi.ts)
	- **Pages / Components:** [frontend/src/pages](frontend/src/pages) and [frontend/src/components](frontend/src/components)

Getting started (development)
-----------------------------

1) Backend (Python / FastAPI)

 - Ensure you have Python 3.10+ and pip available.
 - Create a virtual environment and install dependencies (if you add dependencies to `backend/requirements.txt`, install them; currently the file is empty):

```bash
cd backend
python -m venv .venv
.
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or on cmd
.\.venv\Scripts\activate.bat
pip install -r requirements.txt  # add dependencies here if needed
```

 - By default the backend uses a local SQLite file at `backend/risk.db` (configured in [backend/app/database.py](backend/app/database.py)).
 - Run the FastAPI app (example using Uvicorn):

```bash
cd backend
pip install uvicorn fastapi sqlalchemy pydantic
uvicorn app.main:app --reload --port 8000
```

2) Frontend (Node / Vite)

 - Requires Node.js (18+ recommended) and npm.
 - Install and start the dev server:

```bash
cd frontend
npm install
npm run dev
```

 - The frontend expects the backend API at `http://127.0.0.1:8000` (see [frontend/src/api/eventApi.ts](frontend/src/api/eventApi.ts)). If your backend runs at a different host/port, update that file or use a proxy.

API Endpoints (from backend/app/main.py)
---------------------------------------
- GET /            : Health / simple message
- GET /events      : List all events
- GET /events/{id} : Get event details
- POST /notes      : Add a note (body: `event_id`, `note`)
- GET /events/{id}/notes : Get notes for an event
- PUT /events/{id}/assign : Assign an owner (expects `AssignRequest` and requires manager role via dependency)
- GET /summary     : Summary counts by severity

Notes on implementation
-----------------------
- The backend currently mixes direct route handlers in `main.py` with placeholders for a more modular router/service layout. Several route files and service modules are present but empty — they appear to be scaffolds for future refactor.
- Pydantic schemas in [backend/app/schemas.py](backend/app/schemas.py) contain duplicate class definitions and should be cleaned up.
- The SQLite file is `backend/risk.db`. If you need a clean DB, remove it and let the app recreate tables (or run seed scripts if available).

Running tests
-------------
- Tests are under [backend/tests](backend/tests). Several test files exist but are currently empty; add tests and run with pytest:

```bash
cd backend
pip install pytest
pytest -q
```

Development notes & suggestions
------------------------------
- Clean up duplicate Pydantic models in [backend/app/schemas.py](backend/app/schemas.py).
- Move route handlers out of `main.py` into their respective router modules (several router files are present but empty).
- Implement service layer functions to separate business logic from HTTP handlers.
- Add dependency / requirements to `backend/requirements.txt` so installs are repeatable.
- Fill or remove empty test files and implement CI test workflow.

Where to look first
-------------------
- Backend app entry: [backend/app/main.py](backend/app/main.py)
- DB models: [backend/app/models.py](backend/app/models.py)
- API client usage: [frontend/src/api/eventApi.ts](frontend/src/api/eventApi.ts)
- Frontend router + pages: [frontend/src/App.tsx](frontend/src/App.tsx) and [frontend/src/pages](frontend/src/pages)

If you want, I can next:
- produce a per-file descriptive map for every file in the repo, or
- fix the duplicate Pydantic definitions in `backend/app/schemas.py`, or
- scaffold/implement missing backend routes to match the frontend needs, or
- create a minimal `backend/requirements.txt` and a small README command snippet to run both services together.

Contact
-------
If you want a particular output (per-file map, code cleanup, run scripts, or tests), tell me which and I'll proceed.
