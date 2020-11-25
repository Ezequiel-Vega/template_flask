from flask_script import Server as BaseServer
from app.server import Server
from app import created_app

class APIServer(BaseServer):
    def handle(self, app: Server, *args, **kw):
        app = created_app()
        super(APIServer, self).handle(app, *args, **kw)
