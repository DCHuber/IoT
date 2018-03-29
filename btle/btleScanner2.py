#!/usr/bin/python3

from bluepy.btle import Scanner, DefaultDelegate
import time
import logging
from logging.handlers import TimedRotatingFileHandler

#System now runs as a service, and will require configuration before it will run

#Setup logging information - again, adjust the handler value for where you want to store your log files
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/home/pi/Projects/bluePy/logs/btlescan.csv', when='midnight', backupCount=30, utc=False)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

#Enter an id for the node - recommend the scanner node MAC address.  Ie: "b827eb01c055" 
#You can obtain your devices blue tooth MAC address by executing the command: 'hciconfig'  It will be the "BD Address" value.  
#Remove the ':' between values and change to lower case
nodeID = "b827ebbd5bac"  

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self, dev, isNewDev, isNewData):

		address = dev.addr.replace(":", "")
		if address not in address_dict.keys():
			address_dict[address] = [dev.rssi]
		else:
			address_dict[address].append(dev.rssi)
 
try:
	scanner = Scanner().withDelegate(ScanDelegate())
	address_dict = {}

	while True:    
		
		devices = scanner.scan(5.0)
		for (k,v) in address_dict.items():
			count = len(v)
			average = sum(v) / count
			logger.info('%s,%s,%i,%i', nodeID, k, average, count)

		address_dict = {}
except KeyboardInterrupt:
	logger.info("Shutting down...")
