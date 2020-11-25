from flask import Flask
from flask import jsonify

class Errors(object):
    """
        Clase para el manejo de errores
    """

    def errorhandler(self, app: Flask):
        @app.errorhandler(404)
        def error_404_handle(e):
            response = {
                    'error': True,
                    'msg': 'La URL que quieres ingresar no existe!'
                    }

            return jsonify(response)

        @app.errorhandler(500)
        def error_500_handle(e):
            response = {
                    'error': True,
                    'msg': 'Hubo un error en el servidor de peticiones!'
                    }
