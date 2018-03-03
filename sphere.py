import numpy as np


class Sphere:
    def __init__(self, center, radius):
        self.center = np.array(center)
        self.radius = radius

    def lightness(self, line_vector):
        # camera_origin = np.array([0, 0, 0])
        line_vector = np.array(line_vector) / np.linalg.norm(line_vector)
        assert np.linalg.norm(line_vector) - 1.0 < 1e-3
        a = 1.0
        b = 2.0 * np.dot(line_vector, self.center)
        c = np.linalg.norm(self.center) ** 2 - self.radius ** 2
        test_value = b ** 2.0 - 4.0 * a * c
        return float(test_value > 0)


if __name__ == '__main__':
    s = Sphere([5, 0, 0], 2)
    assert s.lightness(np.array([1, 0, 0])) == 1.0
    assert s.lightness(np.array([0, 1, 0])) == 0.0
    assert s.lightness(np.array([0, 0, 1])) == 0.0
