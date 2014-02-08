#!/srv/robotice/bin/python

import argparse

p = argparse.ArgumentParser(description="Parse command arameters.")

p.add_argument("-p", "--port")
p.add_argument("-a", "--arch")
p.add_argument("-m", "--mode", help="for rpi model GPIO.BCM == expander; GPIO.BOARD")

opts = p.parse_args()

if opts.arch == "armv7l":
import Adafruit_BBIO.ADC as ADC
ADC.setup()
reading = ADC.read(int(opts.port))
if opts.arch == "armv6l":
import RPi.GPIO as GPIO
if opts.mode == 'GPIO.BCM':
GPIO.setmode(GPIO.BCM)
else:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(int(opts.port), GPIO.IN)
reading = GPIO.input(int(opts.port))
if str(reading) == "0":
reading = 1
else:
reading = 0	
GPIO.cleanup()

print reading
exit(0)
