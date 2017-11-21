#!/usr/bin/python3

from w1thermsensor import W1ThermSensor
import requests, json
import logging
from logging.handlers import TimedRotatingFileHandler

#Setup logging information
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/home/pi/Projects/acmeFactory/logs/temp.log', when='midnight', backupCount=30, utc=False)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)


sensor = W1ThermSensor()
tempID = sensor.id

postURL = ''

try:
	rmTemp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
	requests.post(postURL, json={'definition': 'acmeTemps', 'id': tempID, 'tempF':  rmTemp, 'lat': 39.010793, 'lon': -105.050999})
	logger.info('%s,%f', tempID, rmTemp)
except:
	logger.debug ("Error publishing temp")
