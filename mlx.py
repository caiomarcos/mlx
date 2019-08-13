import serial
import io
import numpy as np

print("init")
 
ser = serial.Serial('COM25', 921600)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

value = float(sio.read(5))
mini = 30
maxi = 30

while(True):
	cmd = 768
	while(cmd):
		# line = sio.read(4607)
		value = float(sio.read(5))
		if value < mini:
			mini = value
		if value > maxi:
			maxi = value
		cmd = cmd - 1
	print(maxi)
	print(mini)