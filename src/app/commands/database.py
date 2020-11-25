from flask_script import Manager
from flask_script import prompt_bool
from flask_migrate import stamp

from app.database import sqlAlchemy as db

manager = Manager(help="Operaciones que para manipular la base de datos")

@manager.command
def create():
    """
        Iniciar la base de datos y crear todas las tablas
    """

    # Crear todas las tablas
    db.create_all()

    # Crear la tabla para el control de versiones
    stamp()

@manager.command
def drop():
    """
        Eliminar todas las tablas
    """

    if prompt_bool("Estas seguro de elimar todas las tabla? PERDERAS TODOS LOS DATOS!"):
        db.drop_all()
