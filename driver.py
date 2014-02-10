#!/srv/robotice/bin/python

import argparse

p = argparse.ArgumentParser(description="Parse command parameters.")

p.add_argument("-p", "--port")
p.add_argument("-a", "--arch")
p.add_argument("-m", "--mode")
p.add_argument("-r", "--reverse")

opts = p.parse_args()

arch = opts.arch

if opts.mode == 'on':
    mode = True
else:
    mode = False

if opts.reverse == 'on':
    reverse = True
else:
    reverse = False

if arch == 'armv6l':
    if opts.port.lower().startswith('bmc'):
      bmc = True
      port = opts.port.lower().replace('bmc', '')
    else:
      bmc = False
      port = opts.port

    port = int(port)

else:
    port = opts.port

if arch == "armv7l":

    import Adafruit_BBIO.GPIO as GPIO
     
elif arch == "armv6l":

    import RPi.GPIO as GPIO

    if bmc:
        GPIO.setmode(GPIO.BCM)
    else:
        GPIO.setmode(GPIO.BOARD)

GPIO.setup(port, GPIO.OUT)

if reverse:
    if mode:
        mode = False
    else:
        mode = True

if mode:
    GPIO.output(port, GPIO.HIGH)
else:
    GPIO.output(port, GPIO.LOW)

print "Setting port %s to mode %s, reverse logic: %s" % (port, mode, reverse)

exit(0)
