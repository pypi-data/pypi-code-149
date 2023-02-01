import os
import shutil
import unittest

from hotools.graph import draw_line_graph


class DrawLineGraphTest(unittest.TestCase):
    def test_save_as_image(self):
        if os.path.exists("_temp/"):
            shutil.rmtree("_temp/")
        FILEPATH = "_temp/line_graph.png"
        x = [0, 1, 2]
        y = [0, 1, 2]
        draw_line_graph(x, y, filename=FILEPATH)
        self.assertTrue(os.path.exists(FILEPATH))

    def test_y_ndim(self):
        x = [0, 1, 2]
        y = [[[0, 1, 2], [3, 4, 5]]]
        with self.assertRaises(ValueError):
            draw_line_graph(x, y)

    def test_y_shape(self):
        x = [0, 1, 2]
        y = [0, 1, 2]
        with self.assertRaises(ValueError):
            draw_line_graph(x, y, labels=["Label1", "Label2"])

        y = [[0, 1, 2], [4, 5, 6]]
        with self.assertRaises(ValueError):
            draw_line_graph(x, y, labels=["Label1"])


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    unittest.main()
