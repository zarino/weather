#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use unicode strings by default
from __future__ import unicode_literals

import requests
import requests_cache
import xml.etree.cElementTree as ET

requests_cache.install_cache('weather_cache', expire_after=600)

def get_forecast_data(debug=False):
    """
    Get 48-hour forecast data from yr.no (or local xml file if `debug` is True).
    Return an ElementTree element that you can traverse.
    """
    if debug:
        return ET.parse('forecast_hour_by_hour.xml')
    else:
        xml = requests.get(
            'http://www.yr.no/place/United_Kingdom/England/Liverpool/forecast_hour_by_hour.xml'
        ).text
        return ET.fromstring(xml)

if __name__ == '__main__':

    dom = get_forecast_data

    print dom.find('./location/name').text

    for time in dom.findall('./forecast/tabular/time'):
        print time.get('from'), time.get('to')
        print ' precipitation:', time.find('./precipitation').get('value')
        print ' temperature:', time.find('./temperature').get('value')
        print ' wind:', time.find('./windSpeed').get('mps'), time.find('./windSpeed').get('name')
