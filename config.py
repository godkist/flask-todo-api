import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


def as_bool(value):
    if value:
        return value.lower() in ['true', 'yes', 'on', '1']
    return False


class Config:
    # database options
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_ECHO = as_bool(os.environ.get('SQL_ECHO'))

    # security options
    SECRET_KEY = os.environ.get('SECRET_KEY', 'top-secret!')
