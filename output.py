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

def to_pgm(luminescence_matrix, max_value=255):
    lines = []
    lines.append("P2")
    lines.append("{} {}".format(len(luminescence_matrix[0]),
                                len(luminescence_matrix)))
    lines.append("{}".format(max_value))

    scale = lambda x: min(max_value, max(0, int(x * max_value)))
    for row in luminescence_matrix:
        lines.append(" ".join(((str(scale(k))) for k in row)))

    return "\n".join(lines) + "\n"


if __name__ == '__main__':
    data = to_pgm(ray_tracer.luminescence_from_objects(
            [Sphere([300, 50, 50], 100),
             Sphere([250, -50, -50], 50)]))
    with open("image.pgm", 'w') as f:
        f.write(data)
