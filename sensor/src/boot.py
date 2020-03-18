# This file is executed on every boot (including wake-boot from deepsleep)
import esp

esp.osdebug(None)


import gc

gc.collect()


# Set Up Wifi
from wifi_info import SSID, PASSWORD
import network

# Connect to Wifi
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(SSID, PASSWORD)

# Shutdown Wifi server
ap = network.WLAN(network.AP_IF)
ap.active(False)
