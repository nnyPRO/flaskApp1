import os
from flask import Flask
from werkzeug.debug import DebuggedApplication
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False

app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})


app.config['DEBUG'] = True
app.config['SECRET_KEY'] = \
    '5f0be0bc90b9160b99991d46fbf7f3e924696932925d043c'
app.config['JSON_AS_ASCII'] = False

if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.login_view = 'lab11_login'
login_manager.init_app(app)

from app import views  # noqa
