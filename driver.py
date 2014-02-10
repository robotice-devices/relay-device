#!/srv/robotice/bin/python

import argparse

p = argparse.ArgumentParser(description="Parse command parameters.")

p.add_argument("-p", "--port")
p.add_argument("-a", "--arch")
p.add_argument("-m", "--mode")

opts = p.parse_args()

mode = opts.mode
arch = opts.arch

if arch == 'armv6l' and opts.port.startswith('BMC'):
    bmc = True
    port = opts.port.replace('BMC', '')
else:
    bmc = False
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

if mode == 'on':
    GPIO.output(port, GPIO.HIGH)
else:
    GPIO.output(port, GPIO.LOW)


print reading
exit(0)
