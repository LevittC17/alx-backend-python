#!/usr/bin/env python3

"""
annotate function parameters and return values
with the appropriate types
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing
    an element from lst and its length"""
    return [(i, len(i)) for i in lst]
