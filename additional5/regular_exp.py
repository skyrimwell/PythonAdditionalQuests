import re


def p5(hypertext: str) -> str:
    return re.sub('<[^>]*>', '', hypertext)


def sqrt_func(x: float, epsilon: float) -> float:
    approx = x / 2
    while abs(x - approx) > epsilon:
        approx = 0.5 * (approx + x / approx)
    return approx