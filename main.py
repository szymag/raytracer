import numbers
from math import sqrt
import numpy as np
import imageio
from vec3d import Vec3D
from ray import Ray
from hitable_entities import Sphere, EntityList


nx = 200
ny = 100


def save_ppm(file_name, array):
    imageio.imwrite(file_name + ".ppm", array, format="PPM-FI", flags=1)


def hello_world():
    # First example from tutorial
    array_rgb = np.zeros((ny, nx, 3), dtype=np.uint8)
    array_rgb[:, :, 0] = 255.99 * np.tile(np.arange(0, nx, 1), (ny, 1)) / nx  # red
    array_rgb[:, :, 1] = (
        255.99 * np.transpose(np.tile(np.linspace(ny, 0, num=ny), (nx, 1))) / ny
    )  # green
    array_rgb[:, :, 2] += int(255.99 * 0.2)  # blue
    return array_rgb


def hello_world_vec():
    # Second example from tutorial
    array_rgb = np.zeros((ny, nx, 3), dtype=np.uint8)
    for id, j in enumerate(reversed(range(ny))):
        for i in range(nx):
            array_rgb[id, i, :] = 255.99 * np.array(Vec3D(i / nx, j / ny, 0.2).vector())
    return array_rgb


def first_render():
    # Third example from tutorial
    array_rgb = np.zeros((ny, nx, 3), dtype=np.uint8)
    lower_left_corner = Vec3D(-2, -1, -1)
    horizontal = Vec3D(4, 0, 0)
    vertical = Vec3D(0, 2, 0)
    origin = Vec3D(0, 0, 0)
    world = EntityList(
        [Sphere(Vec3D(0, 0, -1), 0.5), Sphere(Vec3D(0, -100.5, -1), 100)]
    )
    for id, j in enumerate(reversed(range(ny))):
        for i in range(nx):
            u = i / nx
            v = j / ny
            r = Ray(origin, lower_left_corner + u * horizontal + v * vertical)
            array_rgb[id, i, :] = 255.99 * np.array(color(r, world).vector())
    return np.array(array_rgb)


def color(ray, world):
    if world.hit(ray, 0, 1e9):
        return 0.5 * (world.register_hit.normal + Vec3D(1, 1, 1))
    else:
        unit_direction = ray.direction.unit_vector()
        t = 0.5 * (unit_direction.y + 1.0)
        return (1 - t) * Vec3D(1, 1, 1) + t * Vec3D(0.5, 0.7, 1)


if __name__ == "__main__":
    arr_rgb = first_render()
    save_ppm("pic", arr_rgb)
