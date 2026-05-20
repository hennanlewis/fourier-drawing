import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

from core.epicycles import build_epicycles
from core.artists import create_artists
from core.canvas import setup_canvas
from core.trace import Trace

from core.animation_config import (
    FPS,
    ANIMATION_DURATION,
    ANIMATION_INTERVAL,
    MAX_TRACE,
)


class FourierAnimator:
    def __init__(
        self,
        coeffs,
        num_harmonics,
        points
    ):
        self.coeffs = coeffs
        self.points = points

        self.num_harmonics = num_harmonics

        self.total_frames = (ANIMATION_DURATION * FPS)

        self.active_coeffs = (coeffs[:num_harmonics])

        x_limit = np.max(np.abs(points.real))
        y_limit = np.max(np.abs(points.imag))

        limit = math.ceil(max(x_limit, y_limit) / 100) * 100

        self.fig, self.ax = setup_canvas(limit)

        (
            self.vector_lines,
            self.circles,
            self.trace_line,
            self.trace_fill
        ) = create_artists(
            self.ax,
            num_harmonics
        )

        self.trace = Trace(MAX_TRACE)

    def animate(self, frame):
        t = frame / self.total_frames

        vectors, endpoint = build_epicycles(
            self.active_coeffs,
            t,
            self.num_harmonics
        )

        for i, vec in enumerate(vectors):
            sx, sy = vec["start"]
            ex, ey = vec["end"]

            self.vector_lines[i].set_data(
                [sx, ex],
                [sy, ey]
            )

            self.circles[i].center = (
                sx,
                sy
            )

            self.circles[i].radius = vec["radius"]

        MAX_TRACE = 5000

        self.trace.add(endpoint)

        self.trace_line.set_data(
            *self.trace.get_line_data()
        )

        self.trace_fill.set_xy(
            self.trace.get_fill_data()
        )

        return (
            self.vector_lines
            + self.circles
            + [self.trace_line, self.trace_fill]
        )

    def run(self):
        self.anim = FuncAnimation(
            self.fig,
            self.animate,
            frames=self.total_frames,
            interval=ANIMATION_INTERVAL,
            blit=True,
            repeat=False
        )

        plt.show()
