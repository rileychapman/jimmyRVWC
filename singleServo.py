from lib_robotis import *

def to_angle(angle):
	"""
	Move to angle (radians)
	"""

	dyn = USB2Dynamixel_Device('/dev/tty.usbserial-AH01FOVT') #setup usb controller
	servo = Robotis_Servo(dyn, 1, series = 'MX') #setup servo object
	servo.move_angle(angle, angvel = 1.7 , blocking = False)       #(servo id, desired angle, speed, blocking)

#possible locations

# /dev/tty.usbserial-A9GZZXHD 
# /dev/tty.usbserial-AH01FOVT

if __name__ == '__main__':

	command = ''
	while not command == 'end':
		command =  raw_input('rad: ')
		if float(command):
			to_angle(float(command))


