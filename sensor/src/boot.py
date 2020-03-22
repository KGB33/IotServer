# This file is executed on every boot (including wake-boot from deepsleep)
import esp

esp.osdebug(None)


import gc

gc.collect()


# Set Up Wifi
from wifi_info import SSID, PASSWORD
import network

# Shutdown Wifi server
ap = network.WLAN(network.AP_IF)
ap.active(False)

# Connect to Wifi
sta = network.WLAN(network.STA_IF)
sta.active(True)
if not sta.isconnected():
    sta.connect(SSID, PASSWORD)
