import unittest

import numpy as np
from PIL import Image, ImageDraw

from hotools.image_binder import ImageBinder


class ImageBinderTest(unittest.TestCase):
    @staticmethod
    def make_image():
        return ImageBinder(Image.new("RGB", (2, 2), (0, 0, 0)))

    def test_bind_image(self):
        image = self.make_image()
        self.assertEqual(isinstance(image.draw, ImageDraw.ImageDraw), True)

    def test_get_ndarray(self):
        image = self.make_image()
        ndarray = image.get_ndarray()
        ndarray_true = np.zeros((2, 2, 3))
        np.testing.assert_array_equal(ndarray, ndarray_true)

    def test_set_ndarray(self):
        image = self.make_image()
        ndarray1 = image.get_ndarray()
        ndarray1[0][0][0] = 1
        image.set_ndarray(ndarray1)
        ndarray2 = image.get_ndarray()
        np.testing.assert_array_equal(ndarray1, ndarray2)


if __name__ == '__main__':
    unittest.main()
