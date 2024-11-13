# Flask File Extractor

> A lightweight Flask-based web service for extracting text from uploaded files.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python Version](https://img.shields.io/badge/python-%3E%3D%203.11-brightgreen)

CLI: `curl -X POST -F "file=@<file>" http://<host>/extract`

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Endpoints](#api-endpoints)
- [Core Components](#core-components)
- [Deployment](#deployment)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Overview

`Flask File Extractor` enables you to extract text from uploaded files using a simple REST API. This project:

- Accepts file uploads through a POST request.
- Processes files using the `extractous` library.
- Returns extracted text as a JSON response.

## Installation

### Prerequisites

- [Docker](https://www.docker.com/)
- [Fly.io CLI](https://fly.io/docs/getting-started/installing-flyctl/)
- Python 3.11 (for local testing)

### Clone the Repository

```bash  (fetch)
git clone https://github.com/geoffsee/any2text.git
cd any2text
```

### Install Dependencies (for local setup)

```bash
pip install -r requirements.txt
```

## Quick Start

### Using Docker

1. **Build the Docker image:**

   ```bash
   docker build -t flask-file-extractor .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 flask-file-extractor
   ```

### Local Development

To run the Flask app locally:

```bash
python app.py
```

The app will be available at `http://0.0.0.0:5006`.

## API Endpoints

### POST `/extract`

- **Description:** Accepts a file and returns extracted text.
- **Request:**
  - `file` (form-data): The file to upload and process.
- **Response:**
  - `200 OK`: Returns extracted text in JSON format.
  - `400 Bad Request`: If no file is provided or selected.
  - `500 Internal Server Error`: If an error occurs during extraction.

Example Request:

```bash
curl -X POST -F "file=@sample.pdf" http://localhost:5000/extract
```

Example Response:

```json
{
  "text": "Extracted content from the uploaded file."
}
```

## Core Components

### Flask Application

The core of the application is a simple Flask server (`app.py`):

```python
from flask import Flask, request, jsonify
from extractous import Extractor

app = Flask(__name__)
extractor = Extractor()

@app.route("/extract", methods=["POST"])
def extract_text():
    # File upload and text extraction logic
```

### `extractous` Library

This library is used to extract text from uploaded files.

## Deployment

### Deploy on Fly.io

1. **Authenticate with Fly.io:**

   ```bash
   flyctl auth login
   ```

2. **Launch the app:**

   ```bash
   flyctl launch
   ```

3. **Deploy the app:**

   ```bash
   flyctl deploy
   ```

### Docker

For Docker deployment:

```bash
docker build -t flask-file-extractor .
docker run -p 5000:5000 flask-file-extractor
```

## Testing

### Test with Sample File

You can test the API using the `test.sh` script:

```bash
./test.sh
```

This script uploads `sample.pdf` and returns the extracted text.

## Error Handling

The application handles common errors gracefully:

- **File Upload Errors:**
  - If no file is provided:
    ```json
    {"error": "No file provided"}
    ```
  - If no file is selected:
    ```json
    {"error": "No file selected"}
    ```

- **Server Errors:**
  - If an error occurs during extraction:
    ```json
    {"error": "Error message"}
    ```

### Logging

Errors are logged for debugging purposes.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

MIT © 2024 Geoff Seemueller