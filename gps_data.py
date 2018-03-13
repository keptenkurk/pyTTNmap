# gps_data.py
# Wrapper around microGPS.py

from micropygps import MicropyGPS
from machine import UART
import array
import config


class GPS_data():

    def __init__(self):
        self.uart = UART(1, pins=(config.TX, config.RX), baudrate=9600)
        self.gps_dev = MicropyGPS()

    def get_loc(self):
        coords = array.array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0])
        valid = False
        sentence = ''
        # read buffer to last line
        while self.uart.any():
            sentence = self.uart.readline()
        # if timed-out process last line
        if len(sentence) > 0:
            for x in sentence:
                self.gps_dev.update(chr(x))
            if config.DEBUG:
                print(sentence)
                print('Longitude', self.gps_dev.longitude)
                print('Latitude', self.gps_dev.latitude)
                print('UTC Timestamp:', self.gps_dev.timestamp)
                print('Fix Status:', self.gps_dev.fix_stat)
                print('Altitude:', self.gps_dev.altitude)
                print('Horizontal Dilution of Precision:', self.gps_dev.hdop)
                print('Satellites in Use by Receiver:', self.gps_dev.satellites_in_use)
            if self.has_fix:
                valid = True
                timestamp = self.gps_dev.timestamp
                lat = int((self.gps_dev.latitude[0] + (self.gps_dev.latitude[1]/60) + 90)*10000)
                lon = int((self.gps_dev.longitude[0] + (self.gps_dev.longitude[1]/60) + 180)*10000)
                alt = int((self.gps_dev.altitude) * 10)
                lhdop = int((self.gps_dev.hdop) * 10)
                # encode location data
                coords[0] = lat
                coords[1] = (lat >> 8)
                coords[2] = (lat >> 16)
                coords[3] = lon
                coords[4] = (lon >> 8)
                coords[5] = (lon >> 16)
                coords[6] = alt
                coords[7] = (alt >> 8)
                coords[8] = lhdop
        return coords, timestamp, valid

    def has_fix(self):
        return (self.gps_dev.fix_stat > 0 and self.gps_dev.latitude[0] > 0)
