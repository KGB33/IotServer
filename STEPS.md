  1. Tutoraial from [Adafruit](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-for-esp8266)
      > `$PORT` will be like `/dev/ttyUSB0` on Linux/Mac and `COM3` on Windows

      > $BIN_FILE_NAME will be whever was downloaded from the MicroPython website
      * Install `esptool.py`
        >  `poetry add esptool`
      * Delete Flash
        > `esptool.py -p $PORT erase_flash`
      * Install CircuitPython ESP8266 bin
        * Download from tutorial
        * run 
          >`esptool.py -p $PORT write_flash --flash_size=detect -fm dio 0 $BIN_FILE_NAME`

          > `-fm dio` is required for some NodeMCU boards

2. Move files onto board via Ampy
   * First, Install Ampy 
     >  `poetry add adafruit-ampy`

    ### Method 1

    * Move files in sensor to board
      > `ampy put sensor/boot.py`
      > `ampy put sensor/_main.pt main.py`
      > `ampy put sensor/wifi_info.py`

    * Reset
      > `ampy reset`

    * Run Test file
      > `ampy run sensor/test.py`

    ### Method 2
    * Run the install script
      > `python sensor/install.py`


## Wiring
| bme680 | ESP8266 |
|--------|---------|
| VIN    | 3v3     |
| GND    | GND     |
| SCK    | D1      |
| SDI    | D2      |


| dht11 | ESP8266     |
|-------|-------------|
| VIN   | 3v3         |
| GND   | GND         |
| DATA  | D5 (GPIO14) |

![Pinout diagram]()