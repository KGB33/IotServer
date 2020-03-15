# Script to install this package on the board

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="Name of serial port for connected board.")
args = parser.parse_args()

if args.port:
    ampy = f"ampy -p {args.port}"
else:
    ampy = "ampy"

for file_name in ["boot.py", "main.py", "wifi_info.py"]:
    os.system(f"{ampy} put sensor/{file_name}")

os.system(f"{ampy} reset")

os.system(f"{ampy} run sensor/test.py")
