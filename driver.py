#!/srv/robotice/bin/python

import argparse

p = argparse.ArgumentParser(description="Parse command parameters.")

p.add_argument("-p", "--port")
p.add_argument("-a", "--arch")
p.add_argument("-m", "--mode")
p.add_argument("-r", "--reverse")

opts = p.parse_args()

arch = opts.arch #obsolete

try:
    import Adafruit_BBIO.GPIO as GPIO
except Exception, e:
    pass

try:
    import RPi.GPIO as GPIO
except Exception, e:
    pass

if opts.mode == 'on':
    mode = True
else:
    mode = False

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

try:
    if bmc:
        GPIO.setmode(GPIO.BCM)
    else:
        GPIO.setmode(GPIO.BOARD)

    GPIO.setup(port, GPIO.OUT)

    if mode:
        GPIO.output(port, GPIO.HIGH)
    else:
        GPIO.output(port, GPIO.LOW)

    print "Setting port %s to mode %s, reverse logic: %s" % (port, mode, reverse)
except Exception, e:
    print "Missing GPIO library"
finally:
    try:
        GPIO.cleanup()
    except Exception, e:
        pass

exit(0)
