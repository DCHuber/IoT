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
scanner = Scanner()
start = time.time()

while 1:
	end = time.time()
	if ((end - start) > 30):
		devices = scanner.scan(10.0)
		for dev in devices:
			logger.info('%s,%f', dev.addr , dev.rssi)
		start = time.time()
