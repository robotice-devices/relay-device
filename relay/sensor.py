def get_data(sensor):
  """
  Relay status reading
  """

  status_file = '/sys/class/gpio/gpio%s/value' % sensor.get("gpio", sensor.get('port'))

  try:
    f = open(status_file, 'r')
    value = int(f.read())
    f.close()
  except Exception, e:
    raise e
    value = 0

  data = []
  data.append(("%s.socket" % sensor.get('name'), value))
      
  return data