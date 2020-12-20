# To allow the app to be run as a module we register the app's path
import os
import sys

if "app" not in sys.path:
    sys.path.append("app")

from api import *

__all__ = [
    "api",
]
