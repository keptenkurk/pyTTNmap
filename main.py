# main.py
# Main program for a LoPy TTN tracker
#
import gc
import time
import data_display
import pycom
import time
import gps_data
from network import LoRa
import socket
import binascii
import struct

# start the display
disp = data_display.DATA_display()

# Initialize GPS
gps = gps_data.GPS_data()

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)
# join a network using OTAA (Over the Air activation)
app_eui = binascii.unhexlify(config.APP_EUI)
app_key = binascii.unhexlify(config.APP_KEY)
# Join the network
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# Loop until joined
while not lora.has_joined():
    pycom.rgbled(config.YELLOW)
    time.sleep(0.2)
    pycom.rgbled(config.OFF)
    time.sleep(0.2)
pycom.rgbled(config.BLUE)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
# make the socket blocking ? Do we need blocking?
s.setblocking(False)
# set the socket port
s.bind(config.TTN_FPort)

bestdx = 0
flash_color = config.GREEN

while True:
    # start off with a garbaged collected memory
    gc.collect()
    if gps.has_fix():
        flash_color = config.GREEN
    else:
        flash_color = config.BLUE
    gps_array, speed = gps.get_loc()
    if speed >= 0 and gps.has_fix():
        # received valid output
        pycom.rgbled(config.PURPLE)
        try:
            s.send(gps_array)
        except socket.timeout:
            print("Socket timeout on sending")
        s.settimeout(3.0)  # Wait 3 sec for data from gateway
        # format PPGDD  PP=Packets, G=Gateways, DD=max Distance last packet
        try:
            data = s.recv(5)
            if config.DEBUG:
                print(data)
            # decode received packet
            packets = data[1] + 256 * data[0]
            gateways = data[2]
            distance = data[4] + 256 * data[3]
            if distance > bestdx:
                bestdx = distance
            disp.refresh_all(speed, packets, gateways, distance, bestdx)
        except socket.timeout:
            # nothing received
            if config.DEBUG:
                print("No RX downlink data received")
    if speed <= 5:
        update = 27                  # lowest rate: update every 30 sec
    if (speed > 5 and speed <= 25):  # cyling: update every 20 sec
        update = 17
    if speed > 25:                   # driving. update every 10 sec
        update = 7
    # flash led while waiting for next update
    for i in range(0, update):
        gps_array, speed = gps.get_loc()
        disp.refresh_speed(speed)
        pycom.rgbled(flash_color)
        time.sleep(0.1)
        pycom.rgbled(config.OFF)
        time.sleep(0.69)
