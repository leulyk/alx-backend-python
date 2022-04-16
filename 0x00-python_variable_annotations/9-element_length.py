#!/usr/bin/env python3


"""
    Python variable annotations project
    Task 9
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Return a list of tuples of sequences and their length from a
        given iterable containing sequences
    """
    return [(i, len(i)) for i in lst]
