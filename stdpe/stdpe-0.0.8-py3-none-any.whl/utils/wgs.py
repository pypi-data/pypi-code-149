""" World Geodetic System (WGS 84).
    Authors: Joshoua Bigler
"""

import pytz
from datetime import datetime
from dataclasses import dataclass
from timezonefinder import TimezoneFinder



@dataclass
class WGS:
  """ World Geodetic System (WGS 84) """

  lat: float
  lng: float

  def get_utc_offset(self) -> str:
    """ Returns the utc offset of given coordinates. """

    tf = TimezoneFinder()
    tz = tf.timezone_at(lat=self.lat, lng=self.lng)
    offset = datetime.now(pytz.timezone(tz)).strftime('%z')
    return offset
