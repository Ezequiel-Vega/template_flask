from .default import *

APP_ENV = APP_ENV_TESTING

DEBUG = True
TESTING = True

SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost:5432/database_test"
