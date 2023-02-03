import random
import subprocess
from time import sleep
from simulant.keyboard.key import letters


class Keyboard:
    SHIFT_PRESS_TIMEOUT = .1
    REPEAT_TIMEOUT = .1

    def type(self, text):
        codes = []
        for symbol in text:
            delay = random.uniform(.055, .22)
            if symbol.lower() in list(letters.keys()):
                letter = letters.get(symbol.lower())
                before_press = after_press = delay / 2
                if symbol.isupper():
                    sleep(self.SHIFT_PRESS_TIMEOUT)
                    subprocess.call(["simulant", "keydown", 'shift'])
                    sleep(before_press)
                    subprocess.call(["simulant", "keydown", letter])
                    sleep(after_press)
                    subprocess.call(["simulant", "keyup", letter])
                    subprocess.call(["simulant", "keyup", 'shift'])
                else:
                    sleep(before_press)
                    subprocess.call(["simulant", "keydown", letter])
                    sleep(after_press)
                    subprocess.call(["simulant", "keyup", letter])
            else:
                subprocess.call(["simulant", "type", symbol])
                sleep(delay)

        assert all(v == 0 for v in codes)

    def key(self, keyboard_key, repeat=1):
        if repeat > 1:
            counter = repeat
            while counter:
                subprocess.call(["simulant", "key", keyboard_key])
                sleep(self.REPEAT_TIMEOUT)
        else:
            subprocess.call(["simulant", "key", keyboard_key])
