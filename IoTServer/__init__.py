from flask import Flask

from IoTServer.api import api, BME680


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    api.add_resource(BME680, "/bme680/<sensor_id>")

    api.init_app(app)

    return app
