from flask import Flask


from IoTServer.api import api, BME680
from IoTServer.configs import DevelopmentConfig


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    # Api
    api.add_resource(BME680, "/bme680/<sensor_id>")
    api.init_app(app)

    return app
