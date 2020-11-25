from os import environ
from app.server import Server

def created_app() -> Server:
    # Obtener variable de entorno
    settings_module = environ.get('SETTINGS_MODULE_SERVER', 'config.dev')

    # Crear servidor
    app: Server = Server(__name__, settings_module)

    # Iniciar base de datos
    app.init_database()

    # Iniciar migracion
    app.init_migration()

    # Iniciar middlewares
    app.init_middlewares()

    # Iniciar rutas
    app.init_routes()

    # Iniciar errores
    app.init_errors()

    return app
