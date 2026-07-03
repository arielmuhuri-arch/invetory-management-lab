# Inventory Management System

## Description

This project is an inventory management system built with Flask for the backend API and a simple CLI client for interacting with the service.

It supports CRUD operations for inventory items, plus a barcode lookup feature using the OpenFoodFacts API.

The codebase includes:

- `app.py` — Flask REST API server
- `cli.py` — CLI client that talks to the API
- `test_app.py` — unit tests for API endpoints
- `requirements.txt` — required Python dependencies

## Features

- View all inventory items
- Add new inventory items
- Update existing inventory items
- Delete inventory items
- Search an item using an external barcode lookup API
- CLI interface for user interaction
- Unit tests for API functionality

## Project Structure

- `app.py` — defines the Flask application and routes
- `cli.py` — CLI menu to call the API endpoints
- `test_app.py` — tests API endpoints with Flask's test client
- `requirements.txt` — package dependencies for the environment
- `venv/` — local virtual environment (should be ignored in Git)

## API Endpoints

The Flask API runs on `http://127.0.0.1:5000` by default.

- `GET /` — health check endpoint
- `GET /items` — returns the full inventory list
- `POST /items` — adds a new inventory item
- `GET /items/<id>` — returns one item by ID
- `PATCH /items/<id>` — updates one item by ID
- `DELETE /items/<id>` — deletes one item by ID
- `GET /search/<barcode>` — fetches product details from OpenFoodFacts by barcode

## Installation

```bash
git clone <repository-url>
cd inventory-management
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application

1. Start the API server:

```bash
source venv/bin/activate
python3 app.py
```

2. Open a second terminal and run the CLI client:

```bash
source venv/bin/activate
python3 cli.py
```

The CLI uses the API server at `http://127.0.0.1:5000`, so the Flask app must be running first.

## Example CLI Flow

1. Choose `1` to view all items.
2. Choose `2` to add a new item.
3. Choose `3` to search by barcode.
4. Choose `4` to exit.

## Testing

Run the unit tests with:

```bash
source venv/bin/activate
python3 -m pytest -q
```

## Troubleshooting

- If `python3 cli.py` reports a connection error, make sure `app.py` is running.
- Use `python3 -m pytest -q` instead of `python3 pytest`.
- If the CLI cannot connect, verify the API server is listening on `127.0.0.1:5000`.

## Notes

- Keep the virtual environment out of version control by using `.gitignore`.
- The CLI includes error handling for failed API requests.
- This repository is ready for further enhancements, such as persistent storage and user authentication.
