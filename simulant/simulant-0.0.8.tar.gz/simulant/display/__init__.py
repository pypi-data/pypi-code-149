import os
os.environ.get("DISPLAY", os.environ.update({'DISPLAY': ':1'}))
os.environ.get("RESOLUTION", os.environ.update({'RESOLUTION': '1920x1080'}))
from Xlib import display as disp
from Xlib import X
from PIL import Image


class Display:
    @property
    def dsp(self):
        self.dsp = disp.Display()

    def screenshot(self, width=None, height=None):
        image = None
        try:
            scr = self.dsp.screen()
            width = width if width else scr.width_in_pixels
            height = height if height else scr.height_in_pixels
            root = scr.root
            raw = root.get_image(0, 0, width, height, X.ZPixmap, 0xffffffff)
            image = Image.frombytes("RGB", (width, height), raw.data, "raw", "BGRX")
        finally:
            self.dsp.close()
        return image
