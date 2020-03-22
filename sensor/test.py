def test_network_info():
    import network

    sta = network.WLAN(network.STA_IF)
    ap = network.WLAN(network.AP_IF)

    print("\nWifi Info")
    print("\tSTA_IF")
    print("\t  Is Connected: " + str(sta.isconnected()))
    print("\t  Status: " + str(sta.status()))
    print("\t  Active: " + str(sta.active()))
    print("\t  Config: " + str(sta.ifconfig()))

    print("\tAP_IF")
    print("\t  Is Connected: " + str(ap.isconnected()))
    print("\t  Status: " + str(ap.status()))
    print("\t  Active: " + str(ap.active()))
    print("\t  Config: " + str(ap.ifconfig()))


def test_bme680():
    try:
        import main
    except ImportError:
        import _main as main

    print("\nbme680 Sensor Reading:")
    print("\t", main.bme680.get_reading())


def test_dht11():
    try:
        import main
    except ImportError:
        import _main as main

    print("\ndht11 Sensor Reading:")
    print("\t", main.dht11.get_reading())


def test_memory():
    import gc

    free = gc.mem_free()
    used = gc.mem_alloc()
    total = free + used
    print("\nMemory:")
    print("\tFree: ", free, "B")
    print("\tUsed: ", used, "B")
    print("\tTotal: ", total, "B")


def test_requests():
    import requests

    with requests.get("http://api.xively.com/") as r:
        print(r)
        print(r.content)
        print(r.text)
        print(r.content)
        print(r.json())


if __name__ == "__main__":
    test_network_info()
    test_bme680()
    test_dht11()
    test_memory()
    # test_requests()
