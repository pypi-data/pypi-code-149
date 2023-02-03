import sys
from time import sleep

class Typing():
  def type(self, w, delay = 0.25, instant=False, newline=True):
    if instant == True and delay != 0:
      delay = 0
    for char in w:
      sys.stdout.write(char)
      sys.stdout.flush()
      sleep(delay)
    if newline == True:
      print("")
  def colortype(self, w, rgb = [0,0,0], delay=0.25, instant=False, newline=True):
    if instant == True and delay != 0:
      delay = 0
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    sys.stdout.write(f"\033[38;2;{r};{g};{b}m")
    sys.stdout.flush()
    for c in w:
      sys.stdout.write(c)
      sys.stdout.flush()
      sleep(delay)
    if newline == True:
      print("")
    print("\033[0m")
