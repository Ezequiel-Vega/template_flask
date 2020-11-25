from flask import Flask
from .admin import admin_bp
from .auth import auth_bp
from .user import user_bp

class Routes(object):
    """
        Clase para crear e instanciar las rutas de la API
    """

    def register(self, app: Flask):
        """
            Registrar las rutas
            :param app: Aplicacion a donde se van a registrar las rutas
            :type app: Flask
        """
        app.register_blueprint(admin_bp, url_prefix='/api/v1/admin')
        app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
        app.register_blueprint(user_bp, url_prefix='/api/v1/user')
