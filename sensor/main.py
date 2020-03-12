# Setup

# Set Up Wifi
from wifi_info import SSID, PASSWORD
import network


# Connect to Wifi
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(SSID, PASSWORD)

print("STA_IF")
print("  Active: " + str(sta.active()))
print("  Config: " + str(sta.ifconfig()))

# Shutdown Wifi server
ap = network.WLAN(network.AP_IF)
ap.active(False)

print("AP_IF")
print("  Active: " + str(ap.active()))
print("  Config: " + str(ap.ifconfig()))

# Loop
