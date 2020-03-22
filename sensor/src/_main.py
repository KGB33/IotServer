import board
import busio
import microcontroller
import adafruit_bme680
import adafruit_dht
import requests
import time

ESP8266_ID = "".join(str(x) for x in microcontroller.cpu.uid)


class bme680:
    _i2c = busio.I2C(board.SCL, board.SDA)
    _sensor = adafruit_bme680.Adafruit_BME680_I2C(_i2c)
    POST_URL = "http://127.0.0.1:5000/api/v1/bme680/{}".format(ESP8266_ID)

    @classmethod
    def get_reading(cls):
        return {
            "tempature": cls._sensor.temperature,
            "gas": cls._sensor.gas,
            "humidity": cls._sensor.humidity,
            "pressure": cls._sensor.pressure,
        }


class dht11:
    _sensor = adafruit_dht.DHT11(board.GPIO14)

    @classmethod
    def get_reading(cls):
        return {
            "tempature": cls._sensor.temperature,
            "humidity": cls._sensor.humidity,
        }


if __name__ == "__main__":
    print("Url: ", bme680.POST_URL)
    for _ in range(3):
        print(bme680.get_reading())
        time.sleep(0.5)
