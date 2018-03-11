# config.py
# global application parameters
from array import array

# Debuglevels: 0=none, 1=verbose
DEBUG = True

USE_WIFI = False
WIFI_SSID = 'your SSID'
WIFI_PASS = 'your passcode'
WIFI_IP = 'your fixed IP'  # fixed IP
WIFI_SUBNET = 'your netmask'
WIFI_GATEWAY = 'your IPgateway'
WIFI_DNS1 = 'your DNS'

# TTN
# These you need to replace with your own keys (check TTN Console)!
APP_EUI = 'your APP_EUI'
APP_KEY = 'your APP_KEY'

# you can filter that port out in the TTN mapper integration
TTN_FPort = 1

# GPS UART connection
TX = "P11"
RX = "P12"

# Display I2C connection
SDA = "P9"
SCL = "P8"
# Display contrast (1..255)
CONTRAST = 250
# Display SIGNON message
SIGNON = "TTN Tracker    0.9.0"

# Update interval
UPDATE = 30

# led colors
OFF = 0x000000
RED = 0xff0000
BLUE = 0x0000ff
GREEN = 0x00ff00
YELLOW = 0x7f7f00
PURPLE = 0x7f007f

