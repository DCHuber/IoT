from bluepy.btle import Scanner, DefaultDelegate
import time
import logging
from logging.handlers import TimedRotatingFileHandler

# Entry for cron job - adjust to your directories
# * * * * * sudo /usr/bin/python3 /home/pi/Projects/bluePy/btleScanner.py

#Setup logging information
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/home/pi/Projects/bluePy/logs/tile.log', when='midnight', backupCount=30, utc=False)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

nodeID = "<your unique ID>"   #Enter an id for the node - may need to be unique if we get a lot of these on the air

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self, dev, isNewDev, isNewData):
		logger.info('%s,%s,%f', nodeID, dev.addr , dev.rssi)



scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(55.0)

