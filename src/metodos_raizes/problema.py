"""problema das vigas: 1/sqrt(30²-x²) + 1/sqrt(20²-x²) - 1/8 = 0, com 0 < x < 20."""
import math


def f(x):
    return 1 / math.sqrt(900 - x**2) + 1 / math.sqrt(400 - x**2) - 0.125


def df(x):
    return x / (900 - x**2) ** 1.5 + x / (400 - x**2) ** 1.5


def g(x):
    """função de iteração do ponto fixo: x = sqrt(20² - b(x)²)."""
    a = math.sqrt(900 - x**2)
    b = 1 / (0.125 - 1 / a)
    return math.sqrt(400 - b**2)
