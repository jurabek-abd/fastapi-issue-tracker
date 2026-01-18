# Issue Tracker API

A simple REST API for managing issues built with FastAPI.

## Features

- Create, read, update, and delete issues
- Issue priority levels (low, medium, high)
- Issue status tracking (open, in_progress, closed)
- Request timing middleware
- JSON file storage

## Installation

1. Install dependencies:
```bash
pip install fastapi uvicorn pydantic
```

2. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /api/v1/issues` - Get all issues
- `POST /api/v1/issues` - Create a new issue
- `GET /api/v1/issues/{issue_id}` - Get a specific issue
- `PUT /api/v1/issues/{issue_id}` - Update an issue
- `DELETE /api/v1/issues/{issue_id}` - Delete an issue

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
├── main.py                 # Application entry point
├── app/
│   ├── middleware/
│   │   └── timer.py        # Timing middleware
│   ├── routes/
│   │   └── issues.py       # Issue routes
│   ├── schemas.py          # Pydantic models
│   └── storage.py          # JSON file storage 
└── data/
    └── issues.json         # Data storage (auto-created)
```

## Credits

This project is based on the [Traversy Media FastAPI Crash Course](https://youtu.be/8TMQcRcBnW8?si=Lscaupx7UFNgDKYR).
