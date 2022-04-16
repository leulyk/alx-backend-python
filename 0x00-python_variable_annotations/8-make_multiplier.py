#!/usr/bin/env python3

"""
    Python - Variable annotations project
    Task 8
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        A type-annotated function that returns a function
        that multiplies a float by @multiplier
    """
    return lambda value: value * multiplier
