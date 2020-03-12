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
  * Install Ampy
    
    >  `poetry add adafruit-ampy`

  * 