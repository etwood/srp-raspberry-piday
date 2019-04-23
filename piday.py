# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import datetime
import subprocess

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Exit if this is a remote session
# if subprocess.check_output(["tty"]) != "/dev/pts/0\n":
#     print("Exiting since this is a remote session")
#     quit()

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0 # mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# A helpe function to get the current time in a string format
def Now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Main program loop.
while True:
    # Read the ADC channel 0 values 
    solar_value = mcp.read_adc(1)

    # Print the current time and the value read on a line
    print(Now() + ',' +str(solar_value))

    # Pause for second.
    time.sleep(1.0)



