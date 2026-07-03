# Inventory Management System

## Description

A Flask REST API for managing inventory items with CRUD operations and OpenFoodFacts integration.

## Features

- View inventory
- Add inventory
- Update inventory
- Delete inventory
- Search product by barcode
- CLI interface
- Unit tests

## Installation

```bash
git clone <repository-url>
cd inventory-management
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Start the Flask API server first:

```bash
python3 app.py
```

In another terminal, run the CLI:

```bash
python3 cli.py
```

## Testing

Run the unit tests with:

```bash
python3 -m pytest -q
```

## Notes

- Ensure the Flask app is running before using the CLI.
- The CLI now prints informative error messages if the server is unavailable.
