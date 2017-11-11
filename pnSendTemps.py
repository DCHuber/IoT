#!/usr/bin/python

import serial
import time
import logging
from logging.handlers import TimedRotatingFileHandler


from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-6f342924-0468-11e7-b09b-0619f8945a4f"
pnconfig.publish_key = "pub-c-cf8989b3-3f79-4530-a725-b217c702ec59"
pnconfig.ssl = False

pubnub = PubNub(pnconfig)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/var/log/temps/temps.log', when='midnight', backupCount=30, utc=False)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

ser = serial.Serial('/dev/ttyACM0', 9600)

def publish_callback(result, status):
	# check if request successfull
	if not status.is_error():
		pass
	else:
		logger.debug ("Error publishing to pubnub")
		pass

start = time.time()

#Dictionary to hold temperature values.   "eon" is PubNub charting object
temps = {'eon': {}}

while 1:

	#Set the time to determine if we should send data to pubnub
	end = time.time()

	#Grab data from the serial port and convert this to a string
	bytesIn = ser.readline().strip()
	textIn = bytesIn.decode('utf-8')

	#Get the appropriate sensor
	values = textIn.split(':')
	
	#Grab the key : value pairs for the sensor	
	sensor = values[1].strip('\x01')
	temp = float(values[2].strip('\x15\r\n'))
	logger.info('%s,%f', sensor, temp)
	#If the sensor ID is not a key in the dictionary, append it as a new k,v pair  Otherwise update the value
	if sensor not in temps['eon'].keys():
		temps['eon'].update({sensor : temp})
	else:
		temps['eon'][sensor] = temp
	#print(temps)

	#Send data to pubnub if a certain about of seconds have expired
	if ((end - start) > 300) :
		#Send the dictionary to pubnub		
		pubnub.publish().channel('mrTemp').message(temps).async(publish_callback)
		#print("Sent: ")
		#print(temps)

		#reset timer
		start = time.time()	

