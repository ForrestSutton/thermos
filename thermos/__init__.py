import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

from .config import config_by_name

basedir = os.path.abspath(os.path.dirname(__file__))

#configure database
app.config['SECRET_KEY']= '\xb4\xdfj\xd8\n~\x9c\xbc]\xbd\x12S\x8a\xc5\xcb\x05_\xc0\xc4\xf0\xa5\xb0r\xaf'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+ os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True

db = SQLAlchemy(app)

#configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.init_app(app)

#enable debugtoolbar
toolbar = DebugToolbarExtension(app)

#for displaying timestamps
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configure_by_name[config_name])
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)


from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/')

from .bookmarks import bookmarks as bkm_blueprint
app.register_blueprint(bkm_blueprint, url_prefix='/bookmarks')

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

return app
#import models
#import views
