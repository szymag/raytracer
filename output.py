import ray_tracer
from sphere import Sphere


def to_pbm(luminescence_matrix):
    lines = []
    lines.append("P1")
    lines.append("{} {}".format(len(luminescence_matrix[0]),
                                len(luminescence_matrix)))

    for row in luminescence_matrix:
        lines.append(" ".join([str(int(int(k) == 0)) for k in row]))

    return "\n".join(lines) + "\n"


if __name__ == '__main__':
    data = to_pbm(ray_tracer.luminescence_from_objects(
            [Sphere([300, -30, 10], 20),
             Sphere([250, 15, -10], 30)]))
    with open("image.pbm", 'w') as f:
        f.write(data)
