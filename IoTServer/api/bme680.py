from flask_restful import Resource, reqparse

from IoTServer.db import db, SensorQ

parser = reqparse.RequestParser()
parser.add_argument("bme680")


class BME680(Resource):
    def post(self, sensor_id):
        args = parser.parse_args()
        sensor = args["bme680"]
        print(sensor, type(sensor))
        for key, value in sensor["data"]:
            sensor["data"][key] = list(value)

        if db.search(SensorQ.id == sensor_id):
            # update
            return "Updated -- WIP!"
        else:
            return db.insert(sensor)
