from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

class Middlewares(object):
    """
        Clase para instanciar los Middlewares de la API
    """
    def init_cors(self, app: Flask):
        """
            Instanciar CORS
            :param app: Aplicacion a cual se le va a accinar el CORS
            :type app: Flask
        """
        cors: CORS = CORS()

        cors.init_app(
                    app,
                    resources={
                        r"/api/*": {
                            "origins": "*"
                            }
                        }
                )

    def init_jwt(self, app: Flask):
        """
            Instanciar JWT para encriptar tokens
            :param app: Aplicacion a cual se le va a asignar el CORS
            :type app: Flask
        """
        jwt: JWTManager = JWTManager()

        jwt.init_app(app)


    def init_api_key(self, app: Flask):
        """
            Instanciar ```API Key``` para restingir el acceso a la api (Si es privada)
            :param app: Aplicacion a cual se le va a asignar el ```API Key```
            :type app: Flask
        """
        @app.before_request
        def require_api_key():
            key = None

            if 'Api-Key' in request.headers:
                key = request.headers['Api-Key']
            else:
                response = {
                        'error': True,
                        'msg': 'Acceso Denegado! Se necesita una API Key!'
                        }

                return jsonify(response)

            if key != app.config['API_KEY']:
                response = {
                        'error': True,
                        'msg': 'Acceso Denegado! Esta API Key no es valida!'
                        }

                return jsonify(response)
