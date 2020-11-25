from flask_script import Manager
from flask_migrate import MigrateCommand

from app.commands.server import APIServer
from app.commands.database import manager as database_manager

from app import created_app

manager: Manager = Manager(created_app)

manager.add_command('runserver', APIServer())
manager.add_command('migrate', MigrateCommand)
manager.add_command('db', database_manager)
