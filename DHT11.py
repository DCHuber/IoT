#!/usr/bin/python

import sys
import Adafruit_DHT
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

# Using library from Adafruit to interface with DHT11
# https://github.com/adafruit/Adafruit_Python_DHT

postURL = 'https:<host>/acme/add_message'
tempID = "huberDHT11-00001"

try:
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	rmTemp = temperature * 9/5.0 + 32
	requests.post(postURL, json={'definition': 'acmeTemps', 'id': tempID, 'tempF': rmTemp, 'lat': 39.010725, 'lon': -105.050932})
	logger.info('%s,%f', tempID, rmTemp)
except:
	logger.debug ("Error publishing temp")
