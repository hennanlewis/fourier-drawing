from matplotlib.patches import Circle

from core.animation.config import (
    VECTOR_COLOR,
    FILL_COLOR
)


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
