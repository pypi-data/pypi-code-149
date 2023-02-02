""" Threading Event
    Authors: Joel Erzinger
             Joshoua Bigler
"""

import threading

from stdpe.utils.logger import Logger


class Event(threading.Event):
  """ Wrapper for the threading.Event class with extended logging. """

  def __init__(self, name, is_set=False):
    self.name = name
    # self._follows = []
    # self._callbacks = []
    threading.Event.__init__(self)
    threading.Event.set(self) if is_set else None
    Logger()

  def set(self, text: str = '', silent: bool = False):
    msg = f': {text}' if text else ''
    Logger.info(f'[EVENT] {self.name} set ({text})') if not silent else None
    threading.Event.set(self)
    return self

  def clear(self, text: str, silent: bool = False):
    Logger.info(f'[EVENT] {self.name} cleared ({text})') if not silent else None
    threading.Event.clear(self)
    return self

  def wait_for_clearance(self, timeout=None):
    with self._cond:
      signaled = self._flag
      if signaled:
        signaled = self._cond.wait(timeout)
      return signaled

  # def follow(self, event: Event):
  #   self._follows.append(event) if not event in self.following else None
  #   return self

  # @property
  # def following(self) -> list:
  #   return self._follows + [event.following for event in self._follows]

  # def is_set(self) -> bool:
  #   return threading.Event.is_set() or any([event.is_set() for event in self.following])

  # def __nonzero__(self):
  #  return self.is_set()
