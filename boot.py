# boot.py -- run on boot-up
import os
import time
import pycom
import machine
import config
from network import WLAN
from machine import UART

uart = UART(0, 115200)
os.dupterm(uart)

pycom.heartbeat(False)

# Use WiFi AP mode unless USE_WIFI is selected
if config.USE_WIFI:
    pycom.rgbled(0xff0000)  # Waiting for WiFi
    wlan = WLAN()  # get current object, without changing the mode
    if machine.reset_cause() != machine.SOFT_RESET:
        wlan.init(mode=WLAN.STA)

    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=(config.WIFI_IP, config.WIFI_SUBNET, config.WIFI_GATEWAY, config.WIFI_DNS1))

    nets = wlan.scan()

    for net in nets:
        if net.ssid == config.WIFI_SSID:
            if not wlan.isconnected():
                wlan.connect(config.WIFI_SSID, auth=(WLAN.WPA2, config.WIFI_PASS), timeout=5000)
            while not wlan.isconnected():
                machine.idle()  # save power while waiting
            pycom.rgbled(0x00ff00)  # green
            time.sleep(3)
            pycom.rgbled(0x000000)
            break

machine.main('main.py')
