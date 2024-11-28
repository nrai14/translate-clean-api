#Flask's quick start page has set up code
# But this is a better base structure for writing larger applications
# Application will exist in a package -> Subdirectory that has __init__.py = package which can be imported

from flask import Flask

app = Flask(__name__)

# Routes imported at bottom and NOT top
# Workaround to avoid circular imports
from app import routes

# Creates application object as an instance of class Flask imported from the Flask package 