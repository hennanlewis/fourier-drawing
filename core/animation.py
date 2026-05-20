import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

import numpy as np

import math

from core.epicycles import build_epicycles

FPS = 60
ANIMATION_DURATION = 10
ANIMATION_INTERVAL = 100 // FPS

CANVAS_PADDING = 1.5

ASPECT_RATIO = (16, 9)
GRID_DIVISIONS = 20

VECTOR_COLOR = (0, 0, 0, 0.15)
FILL_COLOR = (0, 0, 0, 0.25)
GRID_COLOR = (.55, .55, .55, 0.15)
AXIS_COLOR = (1.0, 0.55, 0.1, 0.8)


def setup_canvas(limit):
    ratio_w, ratio_h = ASPECT_RATIO

    fig_width = 10
    fig_height = (
        fig_width
        * ratio_h
        / ratio_w
    )

    fig, ax = plt.subplots(
        figsize=(
            fig_width,
            fig_height
        )
    )

    ax.set_aspect("equal")

    ax.axis("off")

    padded_limit = (
        math.ceil(
            (limit * CANVAS_PADDING)
            / 100
        ) * 100
    )

    half_width = padded_limit
    half_height = (
        padded_limit
        * ratio_h
        / ratio_w
    )

    ax.set_xlim(
        -half_width,
        half_width
    )

    ax.set_ylim(
        half_height,
        -half_height
    )

    grid_step = (
        half_width * 2
    ) / GRID_DIVISIONS

    x_values = np.arange(
        -half_width,
        half_width + grid_step,
        grid_step
    )

    y_values = np.arange(
        -half_height,
        half_height + grid_step,
        grid_step
    )

    for x in x_values:
        ax.axvline(
            x,
            linewidth=0.5,
            color=GRID_COLOR,
            zorder=0
        )

    for y in y_values:
        ax.axhline(
            y,
            linewidth=0.5,
            color=GRID_COLOR,
            zorder=0
        )

    ax.axvline(
        0,
        linewidth=2,
        color=AXIS_COLOR,
        zorder=1
    )

    ax.axhline(
        0,
        linewidth=2,
        color=AXIS_COLOR,
        zorder=1
    )

    return fig, ax


def create_artists(ax, num_harmonics):
    vector_lines = []
    circles = []

    trace_line, = ax.plot(
        [],
        [],
        linewidth=2,
        color=VECTOR_COLOR,
        alpha=1
    )

    trace_fill = ax.fill(
        [],
        [],
        color=FILL_COLOR
    )[0]

    for _ in range(num_harmonics):
        line, = ax.plot(
            [],
            [],
            linewidth=1,
            alpha=0.5
        )

        circle = Circle(
            (0, 0),
            0,
            fill=False,
            linewidth=1,
            alpha=0.5
        )

        ax.add_patch(circle)

        vector_lines.append(line)
        circles.append(circle)

    return (
        vector_lines,
        circles,
        trace_line,
        trace_fill
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
