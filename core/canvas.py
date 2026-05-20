import matplotlib.pyplot as plt
import numpy as np
import math

from core.animation_config import (
    ASPECT_RATIO,
    GRID_DIVISIONS,
    GRID_COLOR,
    AXIS_COLOR,
    CANVAS_PADDING
)

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
