from sympy import geometry
import numpy as np
from sphere import Sphere

camera_placement = geometry.Point3D(0, 0, 0)
matrix_size = (15, 11)


def pixel_coordinate(matrix_placement):
    return matrix_placement[0] - matrix_size[0]//2, \
           matrix_placement[1] - matrix_size[1]//2


def vector_to_object(pixel):
    assert matrix_size[0] % 2 != 0 and matrix_size[1] % 2 != 0
    return np.array((1, *pixel_coordinate(pixel)))


def vectors_through_matrix():
    sphere = Sphere((5, 0, 0), 4.5)
    luminescence_matrix = np.zeros(matrix_size)
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            luminescence_matrix[i, j] = sphere.lightness(vector_to_object((i, j)))
    return luminescence_matrix


if __name__ == "__main__":
    pass