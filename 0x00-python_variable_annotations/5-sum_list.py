#!/usr/bin/env python3

"""
type-annotated function that takes a list of floats
as arguments and returns their sum as a float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats
    return the result as a float."""
    return sum(input_list)
