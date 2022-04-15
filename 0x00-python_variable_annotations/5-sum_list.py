#!/usr/bin/env python3


"""
    Python - Variable annotations project
    Task 5
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        A type-annotated function that
        return the sum of a list of floating
        point numbers
    """
    return sum(input_list)
