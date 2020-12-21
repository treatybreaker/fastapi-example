# FastAPI Example
A quick and simple FastAPI application that can serve HTML pages via templating or static files.

It takes advantage of FastAPI routers (Blueprints are a rough equivalent in flask)

## Usage (Linux)
1. git clone https://github.com/treatybreaker/fastapi-example.git
2. python -m venv venv/
3. source venv/bin/activate
4. cd fastapi-example
5. pip install .
6. python -m app

## Default routes
- /snake
- /items/id  *id is a number*
- /status
- /docs/  *provided by fastapi*

#### Example Route
http://127.0.0.1:8000/snake/

## Notes
- By default we disable the redoc functionality provided by FastAPI
