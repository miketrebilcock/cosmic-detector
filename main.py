import RPi.GPIO as GPIO
from time import time, gmtime, sleep, strftime
import sys


GM1 = 22
GM2 = 0
logging_time = 60
GM1_TIMES = []
GM1_COUNT = 0
GM2_TIMES = []
GM2_COUNT = 0
#starting	

GPIO.setmode(GPIO.BCM)
GPIO.setup(GM1, GPIO.IN)
GPIO.setup(GM2, GPIO.IN)

def count(channel):
	if channel == GM1:
		GM1_TIMES.append(time()-start_time)
		GM1_COUNT += 1

	if channel == GM2:
		GM2_TIMES.append(time()-start_time)
		GM2_COUNT += 1

start_time = time()

GPIO.add_event_detect(GM1, GPIO.RISING, callback=add_detection)
GPIO.add_event_detect(GM2, GPIO.RISING, callback=add_detection)

while time() < start_time + 60:
	sleep(1)

print 'Finished'
print 'GM1 - Times'
print '-----------'
i=0
while i < len(GM1_TIMES):
	print(GM1_TIMES[i])
	i += 1

print 'GM2 - Times'
print '-----------'
i=0
while i < len(GM2_TIMES):
	print(GM2_TIMES[i])
	i += 1

GPIO.cleanup()