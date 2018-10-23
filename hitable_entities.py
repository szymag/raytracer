import numbers
from math import sqrt
from vec3d import Vec3D
from ray import Ray

class HitRecord:
    def __init__(self, t, p, normal):
        if not isinstance(t, numbers.Real): raise TypeError
        if not isinstance(p, Vec3D): raise TypeError
        if not isinstance(normal, Vec3D): raise TypeError
        self.t = t
        self.p = p
        self.normal = normal


class HitableEntity:
    def __init__(self):
        pass

    def hit(self, ray, t_min, t_max):
        if not isinstance(ray, Ray): raise TypeError
        if not isinstance(t_min, numbers.Real): raise TypeError
        if not isinstance(t_max, numbers.Real): raise TypeError
        return 0


class Sphere(HitableEntity):
    def __init__(self, center, radius):
        if not isinstance(center, Vec3D): raise TypeError
        if not isinstance(radius, numbers.Real): raise TypeError
        HitableEntity.__init__(self)
        self.center = center
        self.radius = radius
        self.record = None

    def hit(self, ray, t_min, t_max):
        oc = ray.origin - self.center
        a = ray.direction @ ray.direction
        b = 2*oc @ ray.direction
        c = oc @ oc - self.radius**2
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            temp = (-b - sqrt(discriminant)) / (2*a)
            return self._check_t_condition(ray, temp, t_min, t_max)
            temp = (-b + sqrt(discriminant)) / (2*a)
            return self._check_t_condition(ray, temp, t_min, t_max)
        return False

    def _check_t_condition(self, ray, t, t_min, t_max):
        if t_min < t and t < t_max:
            self.record = HitRecord(t,
                    ray.point_at_parameter(t),
                    (ray.point_at_parameter(t) - self.center) / self.radius)
            return True


class EntityList(HitableEntity):
        def __init__(self, list):
            HitableEntity.__init__(self)
            self.list = list
            self.record = None

        def hit(self, ray, t_min, t_max):
            hit_entities = [i.record for i in self.list if i.hit(ray, t_min, t_max)]
            if hit_entities:
                self.record = min(hit_entities, key=lambda x: x.t)
                return True
            else:
                return False
