# API Testing Portfolio

Practice project demonstrating REST API testing skills, built while preparing for a Junior AI Agent Developer role. Covers the same core concepts in both Postman (no-code) and Python (code) to show understanding of REST APIs from both angles.

## Contents

- `postman/` — Postman Collection covering HTTP methods, status codes, JSON assertions, pre-request/post-response scripts, authentication, and request chaining.
- `python/` — Python scripts using the `requests` library, covering the same concepts: GET/POST/PUT requests, query parameters, JSON parsing, Basic Auth, Bearer Token authentication (with secrets loaded from environment variables), and multi-step API chaining.

## Topics covered

- HTTP methods and status codes
- Query parameters and request bodies
- JSON parsing and nested data structures
- Response assertions / validation
- Environment variables and secure credential handling (`.env`, never committed)
- Authentication: Basic Auth and Bearer Token
- API chaining (using data from one response in a subsequent request)

## Running the Python scripts

1. Install dependencies:

pip install -r python/requirements.txt

2. Copy `python/.env.example` to `python/.env` and fill in your own values.
3. Run any script, e.g.:

python python/warmup.py

## Postman Collection

Import `postman/REST-API-Examples.postman_collection.json` into Postman to explore the same concepts interactively.