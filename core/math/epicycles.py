import numpy as np

from core.math.models import Epicycle


def build_epicycles(
    coeffs,
    t,
    num_harmonics
):
    x = 0
    y = 0

    vectors = []

    for i in range(num_harmonics):
        c = coeffs[i]

        prev_x = x
        prev_y = y

        freq = c.freq
        amp = c.amp
        phase = c.phase

        angle = (
            2
            * np.pi
            * freq
            * t
            + phase
        )

        x += amp * np.cos(angle)
        y += amp * np.sin(angle)

        vectors.append(
            Epicycle(
                start=(prev_x, prev_y),
                end=(x, y),
                radius=amp
            )
        )

    return vectors, (x, y)