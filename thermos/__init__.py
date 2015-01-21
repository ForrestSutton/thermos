import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#configure database
app.config['SECRET_KEY']= '\xb4\xdfj\xd8\n~\x9c\xbc]\xbd\x12S\x8a\xc5\xcb\x05_\xc0\xc4\xf0\xa5\xb0r\xaf'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+ os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True
db = SQLAlchemy(app)

#configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

#enable debugtoolbar
toolbar = DebugToolbarExtension(app)

#for displaying timestamps
moment = Moment(app)

import models
import views
