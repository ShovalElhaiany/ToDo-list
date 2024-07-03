from os import path
from .src.config import Config
from .src.bluePrint import set_bp, define_blueprints
from .src.requirements import db, login_manager
from .models import User
from .routes import set_routes

from flask import Flask
app = Flask(__name__)

def create_database():
        with app.app_context():
            db.create_all()

        print('Created Database!')

def create_app():
    # Config app
    app.config.from_object(Config)    
    # Init and Create DB
    db.init_app(app)
    create_database()
    # Define Blueprints
    views, auth = define_blueprints()
    # Set Routes
    set_routes(views, auth)
    # Register Blueprints
    set_bp(app, views, auth)
    # Loading user
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    app.app_context().push()

    return app