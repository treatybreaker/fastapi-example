from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.api import application

router = APIRouter()


@router.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return application.templates.TemplateResponse("item.html", {"request": request, "id": id})
