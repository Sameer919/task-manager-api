# Task Manager API

A complete Full Stack Backend Project built with Python Flask for a technical assessment. It provides REST APIs to manage tasks with CRUD operations.

## Features

- RESTful API design
- SQLite Database with SQLAlchemy ORM
- Flask Blueprints for clean code structure
- Data validation and error handling
- Standardized JSON responses

## Prerequisites

- Python 3.8+

## Folder Structure

```
task_manager_api/
├── app/
│   ├── __init__.py       # App factory and database initialization
│   ├── models.py         # SQLAlchemy database models
│   └── routes.py         # API endpoints and logic
├── app.py                # Main application entry point
├── config.py             # Application configuration
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup & Installation

1. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```
*The application will start on http://127.0.0.1:5000 and the database (`tasks.db`) will be created automatically upon the first run.*

## API Endpoints (Postman Examples)

Here are the endpoints you can test. Base URL: `http://127.0.0.1:5000/api/tasks`

### 1. Create a Task (POST)
**URL:** `/api/tasks`
**Headers:** `Content-Type: application/json`
**Body (JSON):**
```json
{
    "title": "Complete technical assessment",
    "description": "Build a Flask API with CRUD operations.",
    "status": "pending"
}
```
*Note: `description` and `status` are optional. `status` defaults to "pending".*

### 2. Get All Tasks (GET)
**URL:** `/api/tasks`
**Response:**
```json
[
    {
        "id": 1,
        "title": "Complete technical assessment",
        "description": "Build a Flask API with CRUD operations.",
        "status": "pending",
        "created_at": "2024-05-05T10:00:00.000000+00:00"
    }
]
```

### 3. Get a Single Task by ID (GET)
**URL:** `/api/tasks/1`
**Response:**
```json
{
    "id": 1,
    "title": "Complete technical assessment",
    "description": "Build a Flask API with CRUD operations.",
    "status": "pending",
    "created_at": "2024-05-05T10:00:00.000000+00:00"
}
```

### 4. Update a Task (PUT)
**URL:** `/api/tasks/1`
**Headers:** `Content-Type: application/json`
**Body (JSON):**
```json
{
    "status": "completed"
}
```

### 5. Delete a Task (DELETE)
**URL:** `/api/tasks/1`
**Response:**
```json
{
    "message": "Task deleted successfully"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Request successful
- `201 Created`: Resource successfully created
- `400 Bad Request`: Invalid input or missing required fields
- `404 Not Found`: Task with the given ID does not exist
