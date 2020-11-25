from flask import Flask

# Base de datos
from app.database import sqlAlchemy
from app.database import migrate

# Middlewares
from app.middlewares import Middlewares

# Rutas
from app.api import Routes

# Errores
from app.errors import Errors

class Server(Flask):
    """
        Clase del servidor de mi aplicacion
    """

    def __init__(self, name: str = "app", settings_module: str = 'config.dev', *args, **kw):
        """
            Constructor de mi servidor
        """

        # Crear servidor de flask
        super(Server, self).__init__(name, *args, *kw)

        # Instanciar configuracion
        self.config.from_object(settings_module)


    def init_database(self):
        """
            Instanciar y configurar base de dados
        """
        sqlAlchemy.init_app(self) 

    def init_migration(self):
        """
            Instanciar y configurar migracion
        """
        migrate.init_app(self, sqlAlchemy)

    def init_middlewares(self):
        """
            Intanciar y configurar Middlewares
        """
        middlewares: Middlewares = Middlewares()

        # Iniciar cors
        middlewares.init_cors(self)

        # Iniciar JWT
        middlewares.init_jwt(self)

        # Iniciar API Key
        middlewares.init_api_key(self)

    def init_routes(self):
        """
            Intanciar y configurar Rutas
        """
        routes: Routes = Routes()

        # Registar rutas
        routes.register(self)

    def init_errors(self):
        """
            Iniciar y configurar manejo de errores
        """
        errors: Errors = Errors()

        # 404 Not Found
        errors.errorhandler(self)
