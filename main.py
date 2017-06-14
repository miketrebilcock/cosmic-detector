import RPi.GPIO as GPIO
from time import time, gmtime, sleep, strftime
import sys


GM1 = 22
GM2 = 0
logging_time = 60
GM1_TIMES = []
GM2_TIMES = []
#starting	

GPIO.setmode(GPIO.BCM)
GPIO.setup(GM1, GPIO.IN)
GPIO.setup(GM2, GPIO.IN)

def count(channel):
	if channel == GM1:
		GM1_TIMES.append(time()-start_time)

	if channel == GM2:
		GM2_TIMES.append(time()-start_time)

start_time = time()

GPIO.add_event_detect(GM1, GPIO.RISING, callback=count)
GPIO.add_event_detect(GM2, GPIO.RISING, callback=count)

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