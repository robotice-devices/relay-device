def get_data(sensor):
  """
  Relay status reading
  """

  status_file = '/sys/class/gpio/gpio%s/value' % sensor.get("gpio", sensor.get('port'))

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