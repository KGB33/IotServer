sta = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)

print("Wifi Info\n")
print("STA_IF")
print("  Active: " + str(sta.active()))
print("  Config: " + str(sta.ifconfig()))


print("AP_IF")
print("  Active: " + str(ap.active()))
print("  Config: " + str(ap.ifconfig()))
