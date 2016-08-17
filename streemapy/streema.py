#!/usr/bin/env python
# -*- coding: utf-8 -*-

#     File:        streema.py
#     Author:      elchinot7
#     Github:      https://github.com/elchinot7
#     Description: Get Info from streema.com
"""
Description: Get Info from streema.com

"""
from __future__ import print_function
import re
import os
try:
    import urllib2
except ImportError:  # Python 3
    import urllib.request as urllib2

__version__= '0.1'

_streema_stations = {
        'abs_class_rock': 'http://nowrelinch.streema.com/nowplaying/18'
        }

def get_streema_info(url):
    """Get info from streema.com radio station

    :url: (str) url to streema.com
    :returns: (str) Artist - Sing Title
    """
    request = urllib2.Request(url)

    response = urllib2.urlopen(request)

    html = response.readlines()
    for line in html:
        if "clean_nowplaying" in line:
            info = line
    match = re.search(r'\s"clean_nowplaying":\s"(.*)",', info)
    if match:
        return match.group(1)
    else:
        return ""

def main():
    """
    Get and print the streema.com NOW_PLAYING info

    """
    STATION = _streema_stations['abs_class_rock']

    if 'ROCK' in os.environ:
        print(get_streema_info(STATION))


if __name__ == "__main__":
    main()
