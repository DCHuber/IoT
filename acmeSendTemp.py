#!/usr/bin/python3

from w1thermsensor import W1ThermSensor
import requests, json
import logging
from logging.handlers import TimedRotatingFileHandler
from time import gmtime, strftime

#Setup logging information
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('/home/pi/Projects/acmeFactory/logs/temp.log', when='midnight', backupCount=30, utc=False)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
sensor = W1ThermSensor()
tempID = sensor.id

postURL = ''

try:
	rmTemp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
	requests.post(postURL, json={'datetime': datetime, 'id': tempID, 'tempF':  rmTemp})
	logger.info('%s,%f', tempID, rmTemp)
except:
	logger.debug ("Error publishing temp")
