from w1thermsensor import W1ThermSensor
import time, requests, json

sensor = W1ThermSensor()
rmTemp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
tempID = sensor.id

postURL = 'http://fedapps.gisinc.com/acme/add_message'

start = time.time()

end = time.time()
if ((end - start) > 300):
	requests.post(postURL, json={'id': tempID, 'tempF':  rmTemp, 'lat': 39.0108867, 'lon': -105.0510984})
	start = time.time()
