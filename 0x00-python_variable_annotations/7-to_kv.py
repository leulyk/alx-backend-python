#!/usr/bin/env python3


"""
    Python - Variable annotations project
    Task 7
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        @k: a string argument
        @v: a integer or a float
        Returns: a tuple with the string and square of the number
    """
    return (k, v * v)
