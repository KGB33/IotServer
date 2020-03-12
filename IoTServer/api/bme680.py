from flask_restful import Resource, reqparse
from tinydb.operations import add

from IoTServer.db import db, SensorQ, append

parser = reqparse.RequestParser()
parser.add_argument("bme680", type=dict)


class BME680(Resource):
    def post(self, sensor_id):
        args = parser.parse_args()
        sensor = args["bme680"]
        if not db.search(SensorQ._id == sensor_id):
            db.insert(
                {
                    "_id": sensor_id,
                    "humidity": [],
                    "temperture": [],
                    "pressure": [],
                    "airQuality": [],
                }
            )

        del sensor["_id"]

        for key, value in sensor.items():
            db.update(append(key, value), SensorQ._id == sensor_id)
