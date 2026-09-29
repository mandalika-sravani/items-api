# Items API

A simple REST API built with Python and Flask for managing a list of items.
It supports creating, reading, updating, and deleting items (CRUD), with
automated linting and tests running on every pull request via GitHub Actions.

![CI](https://github.com/your-username/items-api/actions/workflows/ci.yml/badge.svg)

## Tech Stack

- Python 3.12
- Flask (web framework)
- pytest (testing)
- Ruff (linting)
- GitHub Actions (CI)

## Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:your-username/items-api.git
cd items-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
python app.py
```

The server starts at `http://localhost:5000`.

## API Endpoints

| Method | Endpoint           | Description       | Success Code |
|--------|--------------------|-------------------|--------------|
| GET    | `/health`          | Health check      | 200          |
| GET    | `/items`           | List all items    | 200          |
| POST   | `/items`           | Create an item    | 201          |
| GET    | `/items/<id>`      | Get one item      | 200          |
| PUT    | `/items/<id>`      | Update an item    | 200          |
| DELETE | `/items/<id>`      | Delete an item    | 204          |

### Example requests

```bash
# Create an item
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d "{\"name\": \"book\"}"

# List items
curl http://localhost:5000/items

# Update an item
curl -X PUT http://localhost:5000/items/1 -H "Content-Type: application/json" -d "{\"name\": \"notebook\"}"

# Delete an item
curl -X DELETE http://localhost:5000/items/1
```

## Running Tests and Linting

```bash
pytest -v
ruff check .
```

## Continuous Integration

Every push to `main` and every pull request triggers the GitHub Actions
workflow in `.github/workflows/ci.yml`, which installs dependencies,
runs Ruff, and runs the test suite.

## Project Structure

```
items-api/
├── .github/workflows/ci.yml   # CI pipeline
├── tests/test_app.py          # Test suite
├── app.py                     # Flask application
├── requirements.txt           # Dependencies
├── pyproject.toml             # pytest configuration
├── .gitignore
└── README.md
```

## Git Workflow

This project follows GitHub Flow:

1. Create a feature branch from `main`
2. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `test:`, `chore:`)
3. Open a pull request
4. CI must pass and the PR must be reviewed before merging