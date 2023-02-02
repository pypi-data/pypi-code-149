""" Utitities for the dictionary
    Authors: Joel Erzinger

    Description
    -----------
    Module contains a browser to flatten nested dictionaries.
"""

import json
import numpy as np


class Path(list):

  def __init__(self, path: str = '') -> None:
    self.extend(getattr(self, f"_parse_{path.__class__.__name__}")(path))

  def __str__(self) -> str:
    return f"/{'/'.join(self.path)}"

  def _parse_Path(self, path):
    return path

  def _parse_list(self, path):
    return path

  def _parse_str(self, path):
    return [elem for elem in path.split("/") if elem]

  def __truediv__(self, other):
    return self.copy().extend(Path(other))


class Browser:
  """ Class for browsing and flatten nested dictionaries. """

  def __init__(self, data, **kwargs) -> None:
    self.data = data.data if isinstance(data, Browser) else data
    for key, value in kwargs.items():
      setattr(self, key, value)

  def __repr__(self) -> str:
    return json.dumps(self.data, indent=2, ensure_ascii=False)

  def __iter__(self):
    return self.data.__iter__()

  def sub(self, key, default=None, flatten=False):
    """ Get sub information of given key. """

    flatten = getattr(self, 'flatten', flatten)
    default = getattr(self, 'default', default)
    return Browser(self.get(key, default, flatten), flatten=flatten, default=default)

  def get(self, key, default=None, flatten=False):
    flatten = getattr(self, "flatten", flatten)
    default = getattr(self, "default", default)
    return self._get(self.data, key, default, flatten)

  def _get(self, data, key, default, flatten):
    key = Path(key)
    if type(data) in [list, np.ndarray]:
      result = []
      for value in data:
        value = self._get(value, key, default, flatten) if key else value
        result.extend(value) if flatten and type(value) in [list, np.ndarray] else result.append(value)
      return result
    if not key:
      return data
    if not isinstance(data, dict):
      return default
    if not key[0] in data.keys():
      return default
    return self._get(data[key[0]], key[1:], default, flatten)

  def __truediv__(self, other):
    return self.get(other)

  def __getitem__(self, key):
    return self.get(key)
