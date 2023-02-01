import os
import unittest

from PIL import Image

from hotools.pillow_tools import draw_str_at_center, draw_str_at_point

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


class PillowToolTest(unittest.TestCase):
    @staticmethod
    def make_image():
        return Image.new('RGBA', (256, 256), (0, 0, 127))

    def test_draw_str_at_point(self):
        image = self.make_image()
        draw_str_at_point(
            image,
            "TEST_STRING",
            (10, 10),
            font_path=FONT_PATH,
            fore_ground_color=(0, 0, 0),
            back_ground_color=(255, 255, 255)
        )
        image.save("_temp/draw_str_at_point.png")

    def test_draw_str_at_center(self):
        image = self.make_image()
        draw_str_at_center(
            image,
            "TEST_STRING",
            font_path=FONT_PATH,
            fore_ground_color=(0, 0, 0),
            back_ground_color=(255, 255, 255)
        )
        image.save("_temp/draw_str_at_center.png")


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
