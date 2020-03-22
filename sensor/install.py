# Script to install this package on the board
import time
import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="Name of serial port for connected board.")
parser.add_argument(
    "-w",
    "--wipe",
    help="A compleate wipe of all files and dirs on the board",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--update_libs",
    help="Update required libraires on the board",
    action="store_true",
    default=False,
)
parser.add_argument("--dry_run", action="store_true", default=False)
parser.add_argument("--flash", action="store_true")
parser.add_argument("-d", "--detach", action="store_true")
args = parser.parse_args()

# Constants
BIN_FILE = "flashes/adafruit-circuitpython-feather_huzzah-3.1.2.bin"

CIRCUIT_PYTHON_VERSION = 3
PACKAGE_DIR = (
    f"F:/CircuitPython/v{CIRCUIT_PYTHON_VERSION}/lib"
    if type(CIRCUIT_PYTHON_VERSION) == int
    else f"F:/CircuitPython/py/lib"
)
SUFFIX = ".mpy" if type(CIRCUIT_PYTHON_VERSION) == int else ".py"


if args.port:
    ampy = f"ampy -p {args.port}"
elif args.dry_run:
    ampy = f"echo"
else:
    ampy = "ampy"

# Flash
if args.flash:
    os.system("esptool.py -p COM3 erase_flash")
    os.system(
        f"esptool.py -p COM3 write_flash --flash_size=detect -fm dio 0 {BIN_FILE}"
    )
    time.sleep(2)

# Wipe Board for fresh install
if args.wipe:
    dirs = subprocess.Popen(
        [ampy, "ls"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).communicate()[0]

    dirs = str(dirs, "utf-8").split()
    dirs = [d[1:] for d in dirs]

    print(f"Wiping Drive...")

    for f in dirs:
        if "." in f:
            r = "rm"
        else:
            r = "rmdir"
        out, errs = subprocess.Popen(
            [ampy, r, f], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        ).communicate()
        print(f"\tRemoved {f}")


# Install/Update Packages
if args.update_libs:
    subprocess.run([ampy, "mkdir", "lib"])

    avalible_packages = os.listdir(PACKAGE_DIR)

    required_packages = []
    with open("sensor/requirements.txt", "r") as requirements_file:
        for package in requirements_file.readlines():
            package = package.strip()
            if package in avalible_packages:
                required_packages.append(package)
            elif f"{package}{SUFFIX}" in avalible_packages:
                required_packages.append(f"{package}{SUFFIX}")
            else:
                raise FileNotFoundError(package)

    print("Copying Packages...")
    for package in required_packages:
        subprocess.run([ampy, "put", f"{PACKAGE_DIR}/{package}", f"lib/{package}"])
        print(f"\tCopied {package}")

# Add Our files
print("Copying Source Files...")
for file_name in os.listdir("sensor/src/"):
    os.system(f"{ampy} put sensor/src/{file_name}")
    print(f"\tCopied {file_name}")

# Reset
print("Reseting board...")
os.system(f"{ampy} reset")
time.sleep(0.5)  # Allow board to reset


# Run test script
os.system(f"{ampy} run sensor/test.py")

# Rename main to run detached.
if args.detach:
    os.system(f"{ampy} rm _main.py")
    os.system(f"{ampy} put sensor/src/_main.py main.py")
    os.system(f"{ampy} reset")
