""" StopWatch
    Authors:  Joel Erziner
              Joshoua Bigler

    Description
    -----------
    Contains a stop watch to watch if given time is elapsed 
"""

import time
from dataclasses import dataclass


@dataclass
class Stopwatch():
  """ Contains a stop watch to watch if given time is elapsed. 

      Usage
      -----
      The timer starts when the object is generated.
  """

  hot: bool = False
  starttime: float = time.time() - (99_999_999 if hot else 0)

  def reset(self):
    self.starttime = time.time()

  def elapsed(self, time: float, reset_if_elapsed: bool = False) -> bool:
    """ Checks if given time is elapsed. 
        
        Parameters
        ----------
        time:             time in seconds
        reset_if_elapsed:
     """

    elapsed = self.time > time
    if not elapsed:
      return False
    self.reset() if reset_if_elapsed else None
    return True

  @property
  def time(self):
    return time.time() - self.starttime