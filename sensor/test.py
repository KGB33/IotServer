
def test_network_info():
    sta = network.WLAN(network.STA_IF)
    ap = network.WLAN(network.AP_IF)

    print("Wifi Info\n")
    print("STA_IF")
    print("  Active: " + str(sta.active()))
    print("  Config: " + str(sta.ifconfig()))


    print("AP_IF")
    print("  Active: " + str(ap.active()))
    print("  Config: " + str(ap.ifconfig()))

def test_bme680():
    try:
        import main
    except ImportError:
        import _main as main
    
    print("Sensor Reading:")
    print(main.get_reading())

if __name__ == "__main__":
    test_network_info()
    test_bme680()