from flask import Blueprint

admin_bp : Blueprint = Blueprint("admin", __name__)

from . import routes
