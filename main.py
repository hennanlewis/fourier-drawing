from core.svg.optimizer import unify_svg_paths
from core.svg.loader import sample_svg
from core.math.fourier import compute_fourier
from core.animation.animator import FourierAnimator
import matplotlib.pyplot as plt


INPUT_SVG = "assets/batman.svg"
OUTPUT_SVG = "output/svg/single_path.svg"

NUM_SAMPLES = 2000
NUM_HARMONICS = 100


def main():
    unified_path = unify_svg_paths(
        input_svg=INPUT_SVG,
        output_svg=OUTPUT_SVG
    )

    points = sample_svg(
        unified_path,
        NUM_SAMPLES
    )

    # print(points[:10])
    # print("Total:", len(points))

    coeffs = compute_fourier(points)

    animator = FourierAnimator(
        coeffs=coeffs,
        num_harmonics=NUM_HARMONICS,
        points=points
    )

    animator.export_mp4("output/video/test.mp4")
    # animator.run()

    # plt.plot(points.real, points.imag)
    # plt.gca().invert_yaxis()
    # plt.gca().set_aspect("equal")
    # plt.show()


if __name__ == "__main__":
    main()
