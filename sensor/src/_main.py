import board
import busio
import adafruit_bme680
import time


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)


def get_reading():
    return {
        "tempature": sensor.temperature,
        "gas": sensor.gas,
        "humidity": sensor.humidity,
        "pressure": sensor.pressure,
    }


if __name__ == "__main__":
    for _ in range(5):
        print(get_reading())
        time.sleep(1)
