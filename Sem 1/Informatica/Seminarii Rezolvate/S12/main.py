import run_tests
import data_examples

from logic.domain import GeometricalShape
from application.controller import ShapeController
from ui.console import Console

import numpy as np


def generate_shapes(n):
    """
    Generate the given number of GeometricalShape
    :param n: number of shapes in the resulting list
    :type n: int
    :returns: list with n number shapes
    :rtype: list
    """
    result = []
    for _ in range(n):
        number_of_sides = np.random.randint(3, 12)
        result.append(GeometricalShape(np.random.randint(1, 30, number_of_sides)))
    return result


run_tests.run_all()
print("\n")
data_examples.run_all()
print("\n")

# c = Console(ShapeController(generate_shapes(10)))
# c.start()
