#!/usr/bin/env python3
"""Task 8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """ a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a
    float by multiplier"""

    def multiplication(val: float) -> float:
        return val * multiplier
    return multiplication
