# Inventory Management System

## Overview

This repository contains a Python-based Inventory Management System built with a Flask REST API and a simple command-line interface (CLI).

The application allows users to manage inventory items with create, read, update, and delete (CRUD) operations, and it integrates with the OpenFoodFacts API for barcode-based product lookup.

## Project Contents

- `app.py` — Flask API server with inventory routes and external barcode search.
- `cli.py` — CLI application that communicates with the Flask API.
- `test_app.py` — Unit tests for key API behavior.
- `requirements.txt` — Python dependencies required for the project.
- `README.md` — Project documentation.
- `venv/` — Local virtual environment (excluded from version control).

## Features

- Retrieve all inventory items.
- Add new inventory items.
- Update inventory items by ID.
- Delete inventory items by ID.
- Search for product details using a barcode via OpenFoodFacts.
- CLI interface for easy interaction without a web browser.
- Unit tests for API endpoints.

## API Endpoints

The API runs on `http://127.0.0.1:5000` by default.

- `GET /` — Health check endpoint.
- `GET /items` — Retrieve all inventory items.
- `POST /items` — Add a new inventory item.
- `GET /items/<int:id>` — Get a single item by ID.
- `PATCH /items/<int:id>` — Update an item by ID.
- `DELETE /items/<int:id>` — Remove an item by ID.
- `GET /search/<barcode>` — Lookup product details by barcode.

## Installation

```bash
git clone <repository-url>
cd inventory-management
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the API

Start the Flask server first:

```bash
source venv/bin/activate
python3 app.py
```

The server will listen on `http://127.0.0.1:5000`.

## Running the CLI

Open another terminal, activate the virtual environment, and run:

```bash
source venv/bin/activate
python3 cli.py
```

Use the menu to view items, add items, search by barcode, or exit.

## Testing

Run the test suite with:

```bash
source venv/bin/activate
python3 -m pytest -q
```

## Example Usage

1. Start the API server using `python3 app.py`.
2. Launch the CLI in another terminal with `python3 cli.py`.
3. Choose `1` to list items, `2` to add an item, or `3` to search by barcode.
4. Exit by choosing `4`.

## Troubleshooting

- If the CLI reports a connection error, make sure the Flask API is running.
- Use `python3 -m pytest -q` to run tests, not `python3 pytest`.
- Confirm the server is listening on `127.0.0.1:5000` if external calls fail.

## Notes

- The project currently uses in-memory storage for inventory items.
- The barcode lookup route relies on the OpenFoodFacts API for real-time product information.
- For production use, replace in-memory storage with a database and add authentication.
