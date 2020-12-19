import fastapi
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


class Application:
    """
    Defines the application as a composition of several
    """
    app = fastapi.FastAPI(redoc_url=None)  # Initializing our app

    # Defining our templates directory
    templates = Jinja2Templates(directory=os.path.abspath("app/api/html/templates"))

    # Mounting our static files
    app.mount("/static", StaticFiles(directory=os.path.abspath("app/api/html/static")), name="static")


application = Application()
