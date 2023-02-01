import math
import unittest

import numpy as np

from hotools.transform import (apply_matrix, apply_matrix_at_point,
                               get_rotation_matrix, get_scaling_matrix,
                               get_translation_matrix)


class DrawLineGraphTest(unittest.TestCase):
    def test_translation(self):
        matrix = get_translation_matrix(2.0, 3.0)
        point1 = np.array([1, 1])
        point2 = apply_matrix(matrix, point1)
        np.testing.assert_array_almost_equal(point2, np.array([3.0, 4.0]))

    def test_scaling(self):
        matrix = get_scaling_matrix(2.0)
        point1 = np.array([2, 4])
        point2 = apply_matrix(matrix, point1)
        np.testing.assert_array_almost_equal(point2, np.array([4.0, 8.0]))

    def test_rotation(self):
        matrix = get_rotation_matrix(math.pi)
        point1 = np.array([3, 0])
        point2 = apply_matrix(matrix, point1)
        np.testing.assert_array_almost_equal(point2, np.array([-3.0, 0]))

    def test_apply_matrix_at_point(self):
        scaling_matrix = get_scaling_matrix(2.0)
        scaling_matrix_at_point = apply_matrix_at_point(scaling_matrix, 10.0, 10.0, 0.0)
        point1 = np.array([5, 5])
        point2 = apply_matrix(scaling_matrix_at_point, point1)
        np.testing.assert_array_almost_equal(point2, np.array([0.0, 0.0]))

    def test_use_list(self):
        matrix = get_translation_matrix(2.0, 3.0)
        point1 = [1, 1]
        point2 = apply_matrix(matrix, point1)
        np.testing.assert_array_almost_equal(point2, np.array([3.0, 4.0]))

    def test_use_tuple(self):
        matrix = get_translation_matrix(2.0, 3.0)
        point1 = (1, 1)
        point2 = apply_matrix(matrix, point1)
        np.testing.assert_array_almost_equal(point2, np.array([3.0, 4.0]))

    def test_dimension_error1(self):
        matrix = get_translation_matrix(2.0, 3.0)
        point1 = np.array([[1, 1], [2, 2]])
        with self.assertRaises(ValueError):
            apply_matrix(matrix, point1)

    def test_dimension_error2(self):
        matrix = get_translation_matrix(2.0, 3.0)
        point1 = np.array([1, 1, 1])
        with self.assertRaises(ValueError):
            apply_matrix(matrix, point1)


if __name__ == '__main__':
    unittest.main()
