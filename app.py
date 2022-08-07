
from flask import Flask  # Flask is a class (its uppercase)
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from datetime import datetime as dt


# Config section
class Config():
    # Getting the secret key from the
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # environment; os is a builtin from python
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

# Initializing
app = Flask(__name__)  # app is an instance of Flask;
# creating an instance of a class; The first argument is the name of the
# application’s module or package. __name__ is a convenient shortcut for this
# that is appropriate for most cases.
# This is needed so that Flask knows where to
# look for resources such as templates and static files.
app.config.from_object(Config)   
# want to tell application to use config class we made. so app is instance of your application. 

#init my database manager (aka SQLALchemy) 
db = SQLAlchemy(app) #making instance of SQLAlchemy of that class and passed in into app.
#Needs app configuration and context and everything about the app so it knows how to work.
migrate = Migrate(app, db)



class User(UserMixin, db.Model): #User is the name of the table and keep it 
#singular; inherits from UserMixin; inherits from db as well. Every single 
# database has to inherit db.model (outline for database table). 
# UserMixin has to be first; has to be able 
# to override anything from db.model.
# Now make the columns of your table.
    id = db.Column(db.Integer, primary_key=True)  #primary key
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)

