import numpy as np
import imageio
from vec3d import Vec3D

nx = 200
ny = 100

def save_ppm(file_name, array):
    imageio.imwrite(file_name + ".ppm", array, format="PPM-FI", flags=1)

def hello_world():
    array_rgb = np.zeros((ny, nx, 3), dtype=np.uint8)
    array_rgb[:, :, 0] = 255.99 * np.tile(np.arange(0, nx, 1), (ny, 1)) / nx  # red
    array_rgb[:, :, 1] = (
        255.99 * np.transpose(np.tile(np.linspace(ny, 0, num=ny), (nx, 1))) / ny
    )  # green
    array_rgb[:, :, 2] += int(255.99 * 0.2)  # blue
    return array_rgb

def hello_world_vec():
    arr = np.zeros((ny, nx), dtype=object)
    array_rgb = np.zeros((ny, nx, 3), dtype=np.uint8)
    for i in range(ny, 0):
        for j in range(nx):
            arr[i, j] = 255.99 * Vec3D(i / nx, j / ny, 0)
            array_rgb[i, j, :] = arr[i, j].vector()
    return arr, np.array(array_rgb)

if __name__ == "__main__":
    arr, array_rgb = hello_world_vec()
    save_ppm('pic', array_rgb)
