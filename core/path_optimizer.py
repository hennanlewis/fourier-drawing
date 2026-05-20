from pathlib import Path

from svgpathtools import (
    svg2paths,
    wsvg,
    Path as SVGPath
)

from svgpathtools.path import Line


def complex_distance(a, b):
    return abs(a - b)


def sort_paths(paths):
    remaining = paths.copy()

    ordered = [remaining.pop(0)]

    while remaining:
        current_end = ordered[-1].end

        best_index = None
        best_distance = float("inf")
        reverse = False

        for i, path in enumerate(remaining):
            d_start = complex_distance(
                current_end,
                path.start
            )

            d_end = complex_distance(
                current_end,
                path.end
            )

            if d_start < best_distance:
                best_distance = d_start
                best_index = i
                reverse = False

            if d_end < best_distance:
                best_distance = d_end
                best_index = i
                reverse = True

        next_path = remaining.pop(best_index)

        if reverse:
            next_path = next_path.reversed()

        ordered.append(next_path)

    return ordered


def merge_paths(paths):
    merged = SVGPath()

    for i, path in enumerate(paths):
        if i > 0:
            previous_end = merged[-1].end

            connection = Line(
                previous_end,
                path.start
            )

            merged.append(connection)

        for seg in path:
            merged.append(seg)

    return merged


def unify_svg_paths(input_svg, output_svg):
    output_path = Path(output_svg)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    paths, _ = svg2paths(input_svg)

    ordered = sort_paths(paths)

    merged = merge_paths(ordered)

    wsvg(
        [merged],
        filename=output_svg
    )

    return output_svg
