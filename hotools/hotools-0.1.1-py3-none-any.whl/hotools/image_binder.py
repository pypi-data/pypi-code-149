"""A class to unify Pillow image formats
"""
import numpy as np
from PIL import Image, ImageDraw


class ImageBinder:
    def __init__(self, image: Image):
        self.image: Image = image
        self._update_draw()

    def _update_draw(self):
        self.draw: ImageDraw = ImageDraw.Draw(self.image)

    def get_ndarray(self) -> np.ndarray:
        return np.array(self.image)

    def set_ndarray(self, ndarray: np.ndarray):
        self.image = Image.fromarray(ndarray)
        self._update_draw()
