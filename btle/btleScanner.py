from bluepy.btle import Scanner, DefaultDelegate
import time
import logging
from logging.handlers import TimedRotatingFileHandler

# Entry for cron job - adjust to your directories
# * * * * * sudo /usr/bin/python3 /home/pi/Projects/bluePy/btleScanner.py

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
#Remove the ':' between values
nodeID = "<your unique ID>"   

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self, dev, isNewDev, isNewData):
		for (adtype, desc, value) in dev.getScanData():
			if adtype == 9:    #Has name of device
				device = value
			else:
				device = "unknown"
			
		address = dev.addr.replace(":", "")
		logger.info('%s,%s,%s,%f', nodeID, address, device, dev.rssi)



scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(59.0)
