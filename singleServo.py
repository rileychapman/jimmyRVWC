from lib_robotis import *

def to_angle(angle):
	"""
	Move to angle (radians)
	"""

	dyn = USB2Dynamixel_Device('/dev/tty.usbserial-A9GZZXHD') #setup usb controller
	servo = Robotis_Servo(dyn, 11, 'MX') #setup servo object
	servo.write_id(11) #choose a servo id of our liking
	servo.move_angle(angle,blocking = False)       #(servo id, desired angle, speed, blocking)

