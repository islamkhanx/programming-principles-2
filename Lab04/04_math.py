import math


def degree_to_radian(degree: float) -> float:
    """Python program to convert degree to radian."""
    return degree / 180 * math.pi


def trapezoid_area(a: float, b: float, h: float) -> float:
    """Python program to calculate the area of a trapezoid"""

    return (a + b) * h / 2


def poligon_area(n: int, a: float) -> float:
    "Python program to calculate the area of regular polygon."
    apothem = n / 2 / math.tan(math.pi / n)
    return n * a * apothem / 2


def parrallelogram_area(a: float, h: float) -> float:
    """Python program to calculate the area of a parallelogram."""
    return a * h
