from flask import Blueprint
from .requirements import app

views = Blueprint('views', __name__)
auth = Blueprint('auth', __name__)

def define_blueprints():
    return views, auth

def set_bp(app, views, auth):
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

