"""
All routers MUST include a variable named router which is an APIRouter from fastapi
"""
from .snake import router
from .status import router
from .item import router

# for each route we want to register in this application we should place the router object within this list
__routers__ = [snake.router,
               status.router,
               item.router]

__all__ = ["__routers__"]
