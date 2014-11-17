#!/usr/bin/python

import time
import subprocess
import logging

plain = False

try:
  sys.path.append("/srv/robotice/service")
  from robotice.utils import call_command
except Exception, e:
  plain = True
  LOG.debug("Robotice lib not found")

logger = logging.getLogger("robotice")
logger.setLevel(logging.DEBUG)

python = '/srv/robotice/bin/python2'
executable = '/srv/robotice/drivers/relay/relay/driver.py'

def run(device, model_data, real_data):

  # python driver.py -a armv7l -p P8_10 -m on

  if device.get('reverse', False):

    if int(model_data) == 0:
      command = [python, executable, '-p', str(device.get('port')), '-m', 'off', '-r', 'on']
    else:
      command = [python, executable, '-p', str(device.get('port')), '-m', 'on', '-r', 'on']

  else:

    if int(model_data) == 0:
      command = [python, executable, '-p', str(device.get('port')), '-m', 'off']
    else:
      command = [python, executable, '-p', str(device.get('port')), '-m', 'on']

  if plain is True:
    output = subprocess.check_output(command)
  else:
    output = call_command(command)

  return command, output