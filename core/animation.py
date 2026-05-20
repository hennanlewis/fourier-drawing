import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

from core.epicycles import build_epicycles
from core.artists import create_artists
from core.canvas import setup_canvas

from core.animation_config import (
    FPS,
    ANIMATION_DURATION,
    ANIMATION_INTERVAL,
)

def run_animation(
    coeffs,
    num_harmonics,
    points
):
    total_frames = ANIMATION_DURATION * FPS
    active_coeffs = coeffs[:num_harmonics]

    max_amp = sum(
        c["amp"]
        for c in active_coeffs
    )

    x_limit = np.max(np.abs(points.real))
    y_limit = np.max(np.abs(points.imag))

    limit = math.ceil(
        max(x_limit, y_limit) / 100
    ) * 100

    print("Max amplitude:", max_amp)
    print("Canvas limit:", limit)

    fig, ax = setup_canvas(limit)

    (
        vector_lines,
        circles,
        trace_line,
        trace_fill
    ) = create_artists(
        ax,
        num_harmonics
    )

    trace_x = []
    trace_y = []

    def animate(frame):
        t = frame / total_frames

        vectors, endpoint = build_epicycles(
            active_coeffs,
            t,
            num_harmonics
        )

        for i, vec in enumerate(vectors):
            sx, sy = vec["start"]
            ex, ey = vec["end"]

            vector_lines[i].set_data(
                [sx, ex],
                [sy, ey]
            )

            circles[i].center = (
                sx,
                sy
            )

            circles[i].radius = vec["radius"]

        MAX_TRACE = 5000

        trace_x.append(endpoint[0])
        trace_y.append(endpoint[1])

        trace_line.set_data(
            trace_x,
            trace_y
        )

        trace_fill.set_xy(
            np.column_stack((
                trace_x,
                trace_y
            ))
        )

        return (
            vector_lines
            + circles
            + [trace_line, trace_fill]
        )

    anim = FuncAnimation(
        fig,
        animate,
        frames=total_frames,
        interval=ANIMATION_INTERVAL,
        blit=True,
        repeat=False
    )

    plt.show()
