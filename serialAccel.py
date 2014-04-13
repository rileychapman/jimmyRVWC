import time
import serial
import string

def filter(line):
	numbed = []
	line = line.translate(string.maketrans("\n\r", "  "))
	line = line.strip()
	line = line.split(',')

	for num in line:
		if num == '':
			numbed.append(0)
		else:
			num = float(num)
			numbed.append(num)

	return numbed
	
if __name__ == '__main__':
	ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
	#ser = serial.Serial('/dev/ttyACM0',9600)
	while True:
		lines = []
		for i in range(0,2):
			lines.append(ser.readline())
		#print lines
		result = []
		#for line in lines:
		result.append(filter(lines[1]))
		print result
	



