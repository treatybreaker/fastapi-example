import logging
from .Server import Server, Configuration
from .application import application
from .database import database

log = logging.getLogger(__name__)
# app is defined here so the call to run it in the __main__ file executes properly, take a look
# at the configuration we pass in within the main file to understand why app is defined here again
app = application.app

# Breaking some PEP 8 standard stuff to make it more clear EXACTLY what is happening with registering routes
# PEP 8 is fantastic, but this file is so small that it won't take more than a glance to see this import
from .routers import __routers__

# This may seem like a bad idea as we can now no longer use the functionality provided by include_router from fastapi
# but that same functionality seems to exposed by creating an instance of APIRouter and passing in the correct
# kwargs and as such include_router can be a generic way to include the routes with no loss of function
for router in __routers__:
    app.include_router(router)


@app.on_event("startup")
async def list_routes():
    for route in app.routes:
        # I suspect I am fucking this up, but I'm not going to go digging thus this __dict__ pathing stays
        log.info(f"Registered route {route.__dict__['path']}")


__all__ = [
    "Server",
    "Configuration",
    "routers",
    "application",
    "routers",
    "database"
]
