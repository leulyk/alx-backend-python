#!/usr/bin/env python3

"""
    Python Variable annotations project
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        A type-annotated function that accepts a sequence of
        any type and returns the first element or None
        if the list is none
    """
    if lst:
        return lst[0]
    else:
        return None
