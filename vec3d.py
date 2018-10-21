from math import sqrt, isclose


class Vec3D:
    def __init__(self, e0, e1, e2):
        self.e0 = e0
        self.e1 = e1
        self.e2 = e2

    def __add__(self, other):
        if isinstance(other, Vec3D):
            return Vec3D(self.e0 + other.e0, self.e1 + other.e1, self.e2 + other.e2)
        else:
            raise NotImplementedError

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vec3D):
            return Vec3D(self.e0 - other.e0, self.e1 - other.e1, self.e2 - other.e2)
        else:
            raise NotImplementedError

    def __rsub__(self, other):
        return other - self

    def __matmul__(self, other):
        # dot product
        if isinstance(other, Vec3D):
            return self.dot(other)
        else:
            raise NotImplementedError

    def __rmatmul__(self, other):
        return self @ other

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            # TODO: is it enough?
            return Vec3D(*(n * scalar for n in self.vector()))
        else:
            raise NotImplementedError

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            # TODO: is it enough?
            return Vec3D(*(n / scalar for n in self.vector()))
        else:
            raise NotImplementedError

    def __eq__(self, other):
        return all(a == b for a, b in zip(self.vector(), other.vector()))

    @property
    def x(self):
        return self.e0

    @property
    def y(self):
        return self.e1

    @property
    def z(self):
        return self.e2

    @property
    def r(self):
        return self.e0

    @property
    def g(self):
        return self.e1

    @property
    def b(self):
        return self.e2

    def vector(self):
        # TODO: find better way for returning components
        return self.e0, self.e1, self.e2

    def dot(self, other):
        return sum(a * b for a, b in zip(self.vector(), other.vector()))

    def length(self):
        return sqrt(self.e0 ** 2 + self.e1 ** 2 + self.e2 ** 2)

    def squared_length(self):
        return self.e0 ** 2 + self.e1 ** 2 + self.e2 ** 2

    def unit_vector(self):
        return self / self.length()


if __name__ == "__main__":
    v1 = Vec3D(1, 2, 3)
    v2 = Vec3D(1, 2, 3) * 3
    assert v1.x == v1.r
    assert v1.y == v1.g
    assert v1.z == v1.b
    assert v1 == v1
    assert v2 == Vec3D(3, 6, 9)
    assert v1 + v2 == Vec3D(4, 8, 12)
    assert isclose(v1.length(), sqrt(14))
    assert v1 - v2 == Vec3D(-2, -4, -6)
    assert v2 - v1 == Vec3D(2, 4, 6)
    assert v1 @ v2 == v1.dot(v2) == v2 @ v1
    assert v1 @ v2 == 42
    v1 += v1
    assert v1 == Vec3D(2, 4, 6)
    v3 = Vec3D(1, 0, 0)
    assert v3 == Vec3D(1, 0, 0).unit_vector()
    v4 = Vec3D(1, 1, 1)
    v4.unit_vector()
    assert v4 == Vec3D(1, 1, 1)
