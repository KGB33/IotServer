from flask_restful import Api
from .bme680 import BME680

api = Api(prefix="/api/v1")
