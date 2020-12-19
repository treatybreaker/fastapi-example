# To allow the app to be run as a module we register the app's path
import os
import sys

sys.path.append("app")

from api import *

__all__ = [
    "api",
]
