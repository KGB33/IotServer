import board
import busio
from digitalio import DigitalInOut
import adafruit_requests as requests
import network
import adafruit_esp32spi.adafruit_esp32spi_socket as socket


sta = network.WLAN(network.STA_IF)

requests.set_socket(socket, sta)

ADDRESS = "http://192.168.86.254:5000/api/v1/bme680/01"

TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"

print("Fetching text from %s" % TEXT_URL)
response = requests.get(TEXT_URL)
print("-" * 40)

print("Text Response: ", response.text)
print("-" * 40)
response.close()
