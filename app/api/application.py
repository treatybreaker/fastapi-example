import fastapi
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


class Application:
    """
    Defines the application as a composition of several fastapi application related attributes including the app itself
    """
    app = fastapi.FastAPI(redoc_url=None)  # Initializing our app

    _html_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")
    # Defining our templates directory
    templates = Jinja2Templates(directory=os.path.join(_html_directory, "templates"))

    # Mounting our static files
    app.mount("/static", StaticFiles(directory=os.path.join(_html_directory, "static")), name="static")


application = Application()
