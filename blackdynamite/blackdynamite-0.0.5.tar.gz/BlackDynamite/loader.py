from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
import os
import sys


class Loader:
    def __init__(self, desc="Loading...", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description.
            Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints.
            Defaults to 0.1.
        """
        self.desc = desc
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        if os.isatty(sys.stdout.fileno()):
            self._thread.start()
        else:
            print(f"{self.desc} (please wait)", flush=True)
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self, end=''):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        if os.isatty(sys.stdout.fileno()):
            print("\r" + " " * cols, end="", flush=True)
            print(f"\r{end}", flush=True)
        else:
            print(f"{end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Loading with context manager..."):
        for i in range(10):
            sleep(0.25)

    loader = Loader("Loading with object...", "That was fast!", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()
