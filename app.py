from flask import Flask#Flask is a class (its uppercase)

app = Flask(__name__)#app is an instance of Flask; 
#creating an instance of a class; The first argument is the name of the 
# application’s module or package. __name__ is a convenient shortcut for this 
# that is appropriate for most cases. 
# This is needed so that Flask knows where to 
# look for resources such as templates and static files.
@app.route('/')
def index():
    return "<h1>HI</h1>"

