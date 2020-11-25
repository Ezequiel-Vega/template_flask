from os import environ
from .default import *

APP_ENV = APP_ENV_STAGING

DEBUG = False
TESTING = False

API_KEY = ''

USER_DATABASE = environ.get('USER_DATABASE', 'postgres')
PASSWD_DATABASE = environ.get('PASSWD_DATABASE', 'postgres')
HOST_DATABASE = environ.get('HOST_DATABASE', 'localhost')
PORT_DATABASE = environ.get('PORT_DATABASE', 5432)
NAME_DATABASE = environ.get('NAME_DATABASE', 'database')

SQLALCHEMY_DATABASE_URI = f"postgresql://{USER_DATABASE}:{PASSWD_DATABASE}@{HOST_DATABASE}:{PORT_DATABASE}/{NAME_DATABASE}"
