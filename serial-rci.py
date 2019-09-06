#!/usr/bin/env python3

import sys
import subprocess
import serial
import io
import binascii
from datetime import datetime

ser = serial.Serial()
ser.port = "Com4"
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = None
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write
ser.timeout = 0.5

try:
    ser.open()
except (Exception):
    print ("error open serial port: ")
    exit()

if ser.isOpen():
        ser.flushInput() # flush input buffer, discarding all its contents
        ser.flushOutput() # flush output buffer, aborting current output
        ser.write(bytearray.fromhex("1b 02 08 1b 03"))
        response = (ser.read(11))
        ser.close()
        mybytes = []
        for i in range(0, len(response),1):
            mybytes.append(response[i])
        print(int.from_bytes((mybytes[5:9]), byteorder='little'))
else:
    print("cannot open serial port ")
