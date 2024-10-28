# import string
import urllib.request, urllib.parse, urllib.error
# import urllib.request, urllib.error, urllib.parse
from xml.dom import minidom

WEATHER_URL = 'http://www.google.com/ig/api?weather=%s&hl=%s'


def extract_value(dom, parent, child):
  """Convenience function to dig out weather values."""
  return dom.getElementsByTagName(parent)[0].getElementsByTagName(child)[0].getAttribute('data')


def fetch_weather(location, hl='en-in'):
  """Fetches weather report from Google

  Args:
    location: a zip code (94041); city name, state (weather=Mountain View,CA);...
    hl: the language parameter (language code)

  Returns:
    a dict of weather data.

  """
  url = WEATHER_URL % (urllib.parse.quote(str(location)), hl)
  print(url)
  handler = urllib.request.urlopen(url)
  data = handler.read()
  # print(data)
  dom = minidom.parseString(data)
  handler.close()

  # data = {}
  # weather_dom = dom.getElementsByTagName('weather')[0]
  # data['city'] = extract_value(weather_dom, 'forecast_information','city')
  # data['temperature'] = extract_value(weather_dom, 'current_conditions','temp_f')
  # data['conditions'] = extract_value(weather_dom, 'current_conditions', 'condition')
  # dom.unlink()
  return data