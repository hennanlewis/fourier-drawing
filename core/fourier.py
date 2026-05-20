import numpy as np


def compute_fourier(points):
    N = len(points)
    coeffs = np.fft.fft(points) / N

    freqs = np.fft.fftfreq(N) * N * 2

    result = []

    for coef, freq in zip(coeffs, freqs):
        result.append({
            "freq": freq,
            "amp": np.abs(coef),
            "phase": np.angle(coef),
            "coef": coef
        })

    result.sort(
        key=lambda x: x["amp"],
        reverse=True
    )

    return result