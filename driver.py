#!/srv/robotice/bin/python

import argparse

p = argparse.ArgumentParser(description="Parse command parameters.")

p.add_argument("-p", "--port")
p.add_argument("-m", "--mode")
p.add_argument("-r", "--reverse")

opts = p.parse_args()

device = None

try:
    import Adafruit_BBIO.GPIO as GPIO
    device = 'bbb'
except Exception, e:
    pass

try:
    import RPi.GPIO as GPIO
    device = 'rpi'
except Exception, e:
    pass

if device == None:
    print "Missing GPIO library"
    exit(0)

if opts.mode == 'on':
    mode = True
    mode_data = '1'
else:
    mode = False
    mode_data = '0'

if opts.reverse == 'on':
    reverse = True
else:
    reverse = False

if opts.port.lower().startswith('bmc'):
  bmc = True
  port = opts.port.lower().replace('bmc', '')
else:
  bmc = False
  port = opts.port
try:
    port = int(port)
except Exception, e:
    pass

if reverse:
    if mode:
        mode = False
    else:
        mode = True

if device == 'rpi':
    if bmc:
        GPIO.setmode(GPIO.BCM)
    else:
        GPIO.setmode(GPIO.BOARD)

GPIO.setup(port, GPIO.OUT)

if mode:
    GPIO.output(port, GPIO.HIGH)
else:
    GPIO.output(port, GPIO.LOW)

print "Setting relay at port %s to mode %s, reverse logic: %s" % (port, mode_data, reverse)

exit(0)