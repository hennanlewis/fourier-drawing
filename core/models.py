from dataclasses import dataclass


@dataclass
class FourierTerm:
    freq: float
    amp: float
    phase: float
    coef: complex


@dataclass
class Epicycle:
    start: tuple[float, float]
    end: tuple[float, float]
    radius: float