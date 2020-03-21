import board
import busio
import microcontroller
import adafruit_bme680
import adafruit_requests
import time


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

SENSOR_ID = ''.join(str(x) for x in microcontroller.cpu.uid)
POST_URL = "http://127.0.0.1:5000/api/v1/bme680/{}".format(SENSOR_ID)


def get_reading():
    return {
        "tempature": sensor.temperature,
        "gas": sensor.gas,
        "humidity": sensor.humidity,
        "pressure": sensor.pressure,
    }

def send_reading():
    with adafruit_requests.post() as response:
        pass




if __name__ == "__main__":
    print("Url: ", POST_URL)
    for _ in range(3):
        print(get_reading())
        time.sleep(0.5)
