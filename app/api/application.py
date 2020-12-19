import fastapi
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


class Application:
    """
    Defines the application as a composition of several
    """
    app = fastapi.FastAPI(redoc_url=None)  # Initializing our app

    # Jinja 2 templates can go suck my ball and cocke.
    # These templates point to the BASE package directory, so the "app" directory in this case.
    # This caused me about 5 minutes of headache but still this string declaration shit can go fuck itself
    # As such, assuming we have a start path of app/ we can append further paths so: app/api/html/templates
    templates = Jinja2Templates(directory="api/html/7templates")  # Defining our templates directory

    # Same shit as templates with the strings, I'll string up the fuck who came up with this over path operations >>:((
    app.mount("/static", StaticFiles(directory="api/html/static"), name="static")  # Mounting our static files


application = Application()
