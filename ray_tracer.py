from sympy import geometry
import numpy as np


camera_placement = geometry.Point3D(0, 0, 0)
matrix_size = (151, 101)


def pixel_coordinate(matrix_placement):
    return matrix_placement[0] - matrix_size[0]//2, \
           matrix_placement[1] - matrix_size[1]//2


def vector_to_object(pixel):
    assert matrix_size[0] % 2 != 0 and matrix_size[1] %2 != 0
    return [geometry.Point3D((1, *pixel_coordinate(pixel))), camera_placement]


def vectors_through_matrix():
    luminescence_matrix = np.zeros(matrix_size)
    return luminescence_matrix


if __name__ == "__main__":
    pass