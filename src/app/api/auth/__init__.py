from flask import Blueprint

auth_bp : Blueprint = Blueprint("auth", __name__)

from . import routes
