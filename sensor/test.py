def test_network_info():
    sta = network.WLAN(network.STA_IF)
    ap = network.WLAN(network.AP_IF)

    print("\nWifi Info")
    print("STA_IF")
    print("  Is Connected: " + str(sta.isconnected()))
    print("  Status: " + str(sta.status()))
    print("  Active: " + str(sta.active()))
    print("  Config: " + str(sta.ifconfig()))

    print("AP_IF")
    print("  Is Connected: " + str(ap.isconnected()))
    print("  Status: " + str(ap.status()))
    print("  Active: " + str(ap.active()))
    print("  Config: " + str(ap.ifconfig()))


def test_bme680():
    try:
        import main
    except ImportError:
        import _main as main

    print("\nSensor Reading:")
    print(main.get_reading())


def test_memory():
    import gc

    free = gc.mem_free()
    used = gc.mem_alloc()
    total = free + used
    print("\nMemory:")
    print("\tFree: ", free, "B")
    print("\tUsed: ", used, "B")
    print("\tTotal: ", total, "B")


if __name__ == "__main__":
    test_network_info()
    test_bme680()
    test_memory()
