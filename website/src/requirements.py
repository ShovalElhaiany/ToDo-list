from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app: Flask = Flask(__name__)
db: SQLAlchemy = SQLAlchemy()
login_manager: LoginManager = LoginManager()