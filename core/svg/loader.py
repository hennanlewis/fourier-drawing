import numpy as np

from svgpathtools import svg2paths


DRAWING_SCALE = 3


def normalize_points(points):
    center = np.mean(points)

    centered = points - center

    return centered * DRAWING_SCALE


def sample_svg(svg_file, num_samples):
    paths, _ = svg2paths(svg_file)

    if not paths:
        raise ValueError("Nenhum path encontrado")

    path = paths[0]

    points = np.array([
        path.point(t)
        for t in np.linspace(0, 1, num_samples)
    ])

    return normalize_points(points)
