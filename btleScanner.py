from bluepy.btle import Scanner, DefaultDelegate
import time
import logging
from logging.handlers import TimedRotatingFileHandler

#Setup logging information
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/home/pi/Projects/bluePy/logs/tile.log', when='midnight', backupCount=30, utc=False)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self, dev, isNewDev, isNewData):
		logger.info('%s,%f', dev.addr , dev.rssi)



scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(30.0)

