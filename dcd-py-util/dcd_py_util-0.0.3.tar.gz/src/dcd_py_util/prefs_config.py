import json
import pathlib
import os

PREFS_FILEPATH = str(pathlib.Path().absolute())
PREFS_FILENAME = os.path.join(PREFS_FILEPATH, 'prefs_config.json')


class Preferences:
    _initialized = False

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self._prefs = {}
            if os.path.exists(PREFS_FILENAME) and os.path.isfile(
                    PREFS_FILENAME):
                try:
                    with open(PREFS_FILENAME, encoding='utf-8') as json_file:
                        self._prefs = json.load(json_file)
                except OSError:
                    raise ValueError(
                        'Error importing JSON preferences from file {}.'
                        .format(PREFS_FILENAME))
            else:
                self.save_prefs()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Preferences, cls).__new__(cls)
        return cls._inst

    def get_prefs(self) -> dict:
        return self._prefs

    def save_prefs(self) -> bool:
        _result = False
        try:
            with open(PREFS_FILENAME, 'w', encoding='utf-8') as json_file:
                json.dump(self._prefs, json_file)
                _result = True
        except OSError:
            raise ValueError(
                'Error saving JSON preferences to file {}.'.format(
                    PREFS_FILENAME))
        return _result
