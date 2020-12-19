from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.api import application
import aiofiles

router = APIRouter()

with aiofiles.open("some_file") as file:
    print(file)


@router.get("/snake", response_class=HTMLResponse)
async def serve_snake(request: Request):
    return application.templates.TemplateResponse("snake.html", {"request": request})
