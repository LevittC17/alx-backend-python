#!/usr/bin/env python3

"""
type-annotation function that takes a string and
an int OR float as arguments and returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k as the first element and the square
    of v as the second element"""
    return (k, float(v ** 2))
