
import sys
import logging

LOG = logging.getLogger("relay.sensor")

try:
  sys.path.append("/srv/robotice/service") # if will be installed over pip or has dir in PYTHONPATH not needed
  from robotice.utils.platform.bb import BB_PIN_2_GPIO_MAP
except Exception, e:
  LOG.warning("Missing Robotice lib, now support only PINs like a P9_40")

def get_data(sensor):
  """
  Relay status reading
  """
  status_file = None

  if not "P" in sensor.get('port'):
    status_file = '/sys/class/gpio/gpio%s/value' % sensor.get('port')
  else:
    try:
      if sensor.get('port') in BB_PIN_2_GPIO_MAP:
        status_file = '/sys/class/gpio/gpio%s/value' % str(BB_PIN_2_GPIO_MAP[sensor.get('port')])
      else:
        raise Exception("PIN {0} was not found in {1}".format(sensor.get('port'), BB_PIN_2_GPIO_MAP))
    except Exception, e:
      raise e

  if not status_file:
    raise Exception("Status file not constructed for %s" % sensor)

  try:
    f = open(status_file, 'r')
    value = int(f.read())
    f.close()

    if sensor.get('reverse', False):
      if value == 0:
        value = 1
      if value == 1:
        value = 0

  except Exception, e:
    raise e
    value = 0

  data = []
  data.append(("%s.socket" % sensor.get('name'), value))
      
  return data