from flask import Flask  # Flask is a class (its uppercase)
import os

# Config section
class Config():
    # Getting the secret key from the
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # environment; os is a builtin from python

# Initializing
app = Flask(__name__)  # app is an instance of Flask;
# creating an instance of a class; The first argument is the name of the
# application’s module or package. __name__ is a convenient shortcut for this
# that is appropriate for most cases.
# This is needed so that Flask knows where to
# look for resources such as templates and static files.
app.config.from_object(Config)   
# want to tell application to use config class we made. so app is instance of your application. 

# routes
@app.route('/')
def index():
    return "<h1>HI</h1>"
