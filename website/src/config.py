from .utils import generate_secret_key

class DB():
    USER_NAME = 'root'
    PASSWORD = 'Shoval963654'
    HOST = 'localhost'
    PORT = '3306'
    SCHEMA = 'to_do_list'

class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB.USER_NAME}:{DB.PASSWORD}@{DB.HOST}:{DB.PORT}/{DB.SCHEMA}'
    SECRET_KEY = generate_secret_key()