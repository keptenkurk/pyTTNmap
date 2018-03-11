# data_display.py
# Class which updates the display in 2 ways
# * refresh_speed: update global speed value each second
# * refresh_all: update entire display by calling refresh_data
# uses:
#   lopylcd:    a simplified i2c 128x64 display driver
#   config:     global application parameters
#
import lopylcd
import config


class DATA_display():

    speed = 0
    packets = 0
    gateways = 0
    distance = 0
    bestdx = 0

    def __init__(self):
        self.display = lopylcd.lopylcd(config.SDA, config.SCL)
        self.refresh_all(self.speed, self.packets,
                         self.gateways, self.distance, self.bestdx)

    def refresh_all(self, speed, packets, gateways, distance, bestdx):
        self.speed = speed
        self.packets = packets
        self.gateways = gateways
        self.distance = distance
        self.bestdx = bestdx
        if self.display.isConnected():
            self.display.set_contrast(config.CONTRAST)
            self.display.displayOn()
            self.display.clearBuffer()
            self.display.addString(0, 0, config.SIGNON)
            self.display.addString(0, 1, "--------------------")
            self.display.addString(0, 2, "Speed:      {:3d} km/h".format(self.speed))
            self.display.addString(0, 3, "                    ")
            self.display.addString(0, 4, "Packets:       {:5d}".format(self.packets))
            self.display.addString(0, 5, "Gateways:        {:3d}".format(self.gateways))
            self.display.addString(0, 6, "Last dist:   {:5d} m".format(self.distance))
            self.display.addString(0, 7, "Max  dist:   {:5d} m".format(self.bestdx))
            self.display.drawBuffer()
        else:
            print("Error: LCD not found")

    def refresh_speed(self, speed):
        self.speed = speed
        if self.display.isConnected():
            self.display.addString(0, 2,  "Speed:      {:3d} km/h".format(self.speed))
            self.display.drawBuffer()
        else:
            print("Error: LCD not found")
