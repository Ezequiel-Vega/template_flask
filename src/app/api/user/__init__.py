from flask import Blueprint

user_bp : Blueprint = Blueprint("user", __name__)

from . import routes
