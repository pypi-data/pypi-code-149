"""Transform
"""
import math
from typing import Union

import numpy as np


def get_translation_matrix(x: float, y: float) -> np.ndarray:
    return np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])


def get_scaling_matrix(scale: float) -> np.ndarray:
    return np.array([[scale, 0, 0], [0, scale, 0], [0, 0, 1]])


def get_rotation_matrix(angle: float) -> np.ndarray:
    return np.array([[math.cos(angle), math.sin(angle), 0], [-math.sin(angle), math.cos(angle), 0], [0, 0, 1]])


def apply_matrix_at_point(matrix: np.ndarray, x: float, y: float, offset: float) -> np.ndarray:
    """Convert an arbitary coordinate transformation matrix(scaling or rotation etc.) to
    one originating at arbitary coordinate.

    Args:
        matrix: An coordinate transformation matrix to convert.
        x: x-coordinate of the origin to convert.
        y: y-coordinate of the origin to convert.
        offset: An offset of translation(if the matrix is converting vertices then 0, converting images then 0.5).

    Returns:
        A result of the coordinate transformation matrix.

    """
    translation_matrix = get_translation_matrix(-x + offset, -y + offset)
    translation_matrix_inv = np.linalg.inv(translation_matrix)
    return translation_matrix_inv @ matrix @ translation_matrix


def apply_matrix(matrix: np.ndarray, point1: Union[np.ndarray, list, tuple]) -> np.ndarray:
    if type(point1) is not np.ndarray:
        if type(point1) is list or type(point1) is tuple:
            point1 = np.array(point1)
        else:
            raise ValueError(f"The type of coordinate（{type(point1)}）is incorrect.")

    shape = point1.shape
    if len(shape) != 1:
        raise ValueError(f"The dimension of the coordinate array {len(shape)}）must be 1.")
    if shape[0] != 2:
        raise ValueError(f"The size of array（{shape[0]}）must be 2.")

    point2 = np.dot(matrix, np.append(point1, 1.0))
    return point2[:2]
