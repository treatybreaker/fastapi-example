# FastAPI Example

## Usage (Linux)
1. git clone https://github.com/treatybreaker/fastapi-example.git
2. git pull
3. python -m venv venv/
4. source venv/bin/activate
5. cd fastapi-example
6. pip install .
7. python -m app

## Default routes
- /snake
- /items/id  *id is a number*
- /status
- /docs/  *provided by fastapi*

#### Example Route
http://127.0.0.1:8000/snake/

## Notes
- By default we disable the redoc functionality provided by FastAPI
