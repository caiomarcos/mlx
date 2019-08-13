import serial
import io
import numpy as np

print("init")

ser = serial.Serial('COM25', 921600)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

cmd = True

while(cmd):
	# line = sio.read(4607)
	line = sio.readline()
	print(line)