from vec3d import Vec3D


class Ray:
    def __init__(self, origin, direction):
        if isinstance(origin, Vec3D):
            self.origin = origin
        else:
            raise TypeError("origin is a vec3d object")
        if isinstance(direction, Vec3D):
            self.direction = direction
        else:
            raise TypeError("origin is a vec3d object")

    @property
    def A(self):
        return self.origin

    @property
    def B(self):
        return self.direction

    def point_at_parameter(self, t):
        return self.origin + self.direction*t


if __name__ == "__main__":
    r = Ray(Vec3D(0, 0, 0), Vec3D(0, 0, 1))
    assert r.point_at_parameter(1) == Vec3D(0, 0, 1)
    assert r.direciton == r.B
