# data_display.py
# Class which updates the display in 2 ways
# * refresh_timestamp: update UTC GPS received time each second
# * refresh_all: update entire display by calling refresh_data
# uses:
#   lopylcd:    a simplified i2c 128x64 display driver
#   config:     global application parameters
#
import lopylcd
import config


class DATA_display():

    timestamp = (0, 0, 0)
    packets = 0
    gateways = 0
    distance = 0
    bestdx = 0

    def __init__(self):
        self.display = lopylcd.lopylcd(config.SDA, config.SCL)
        self.refresh_all(self.timestamp, self.packets,
                         self.gateways, self.distance, self.bestdx)

    def refresh_all(self, timestamp, packets, gateways, distance, bestdx):
        self.timestamp = timestamp
        self.packets = packets
        self.gateways = gateways
        self.distance = distance
        self.bestdx = bestdx
        if self.display.isConnected():
            self.hh = self.timestamp[0]
            self.mm = self.timestamp[1]
            self.ss = self.timestamp[2]
            self.display.set_contrast(config.CONTRAST)
            self.display.displayOn()
            self.display.clearBuffer()
            self.display.addString(0, 0, config.SIGNON)
            self.display.addString(0, 1, "--------------------")
            self.display.addString(0, 2, "UTC Time:   {:02d}:{:02d}:{:02.0f}"
                                   .format(self.hh, self.mm, self.ss))
            self.display.addString(0, 3, "                    ")
            self.display.addString(0, 4, "Packets:       {:5d}".format(self.packets))
            self.display.addString(0, 5, "Gateways:        {:3d}".format(self.gateways))
            self.display.addString(0, 6, "Last dist:   {:5d} m".format(self.distance))
            self.display.addString(0, 7, "Max  dist:   {:5d} m".format(self.bestdx))
            self.display.drawBuffer()
        else:
            print("Error: LCD not found")

    def refresh_timestamp(self, timestamp):
        self.hh = timestamp[0]
        self.mm = timestamp[1]
        self.ss = timestamp[2]
        if self.display.isConnected():
            self.display.addString(0, 2, "UTC Time:   {:02d}:{:02d}:{:02.0f}"
                                   .format(self.hh, self.mm, self.ss))
            self.display.drawBuffer()
        else:
            print("Error: LCD not found")
