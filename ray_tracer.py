from sympy import geometry
import numpy as np
from sphere import Sphere
import collections

camera_placement = geometry.Point3D(0, 0, 0)
matrix_size = (151, 151)
light_position = np.array([0, 0, 0])

def pixel_coordinate(matrix_placement):
    return matrix_placement[0] - matrix_size[0] // 2, \
           matrix_placement[1] - matrix_size[1] // 2


def vector_to_object(pixel):
    assert matrix_size[0] % 2 != 0 and matrix_size[1] % 2 != 0
    return np.array((100.0, *pixel_coordinate(pixel)))


def luminescence_from_objects(objects):
    luminescence_matrix = np.zeros(matrix_size)
    assert isinstance(objects, collections.Iterable)
    for i in objects:
        luminescence_matrix = np.maximum(vectors_through_matrix(i), luminescence_matrix)
    return luminescence_matrix


def vectors_through_matrix(object):
    assert isinstance(object, Sphere)  # Update for other type of objects
    luminescence_matrix = np.zeros(matrix_size)
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            luminescence_matrix[i, j] = object.lightness(vector_to_object((i, j)), light_position)
    return luminescence_matrix


if __name__ == "__main__":
    pass
