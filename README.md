# pyTTNmap: a TTN tracker for LoPy  v1.0.0
Python code to track the location of a LoPy TTN node to TTNmapper

# Blog info
https://keptenkurk.wordpress.com/2018/03/05/mapping-the-things-network-with-a-lopy-1/

# Uses:
* Pycom LoPy ver 1.17.0.b1 (not tested on LoPy4 or earlier firmwares)
* Connected GPS VK2828U8G5LF
    Configured for NMEA GPGGA sentences only at a rate of 1/s
* Connected display SSD1306 128x64 I2C
* Connected LoRa antenna and located in range of a LoRa gateway
* A Node-Red application consuming the data and replying to the node


# Description
The LoRa TTN tracker receives its location from the connected GPS
This is send over LoRa - depending on the speed - at every 10..30 seconds.
The TTN Mapper integration on The Things Network consumes the data and uses it for generating the coverage maps
The Node-Red application also consumes the data and replies to the node the recored distance 
(or max distance if more gateways received the packet), the total number of received packets, the number of 
unique gateways which received a packet and the longest distance recorded in the entire session.
This data is then displayed on the TTN tracker itself.

# Following steps will be performed after reboot:
1. Led falshes RED while waiting for WiFi (if configured)
2. Display initializes at all "0"
3. Led flashes YELLOW while waiting for OTAA registration on the LoRa network. Depending on nearby gateway availability this may take a while
4. Led flashes BLUE while waiting for GPS fix. Depending on the skyview this might take a while.
5. Led flashes GREEN. Yes! You're there. The location will be sent roughly every 10 seconds. While sending and waiting for a reply from the network the led will be PURPLE
6. Received data will be shown on the display and the time should show the actual UTC time. During LoRa transmit/receive the time will stop for a few seconds.

