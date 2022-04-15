#!/usr/bin/env python3

"""
    Python - Variable annotations project
    Task 6
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
        A type-annotated function that computes the sum
        of a list of integers and floating point numbers
    """
    return sum(mxd_list)
