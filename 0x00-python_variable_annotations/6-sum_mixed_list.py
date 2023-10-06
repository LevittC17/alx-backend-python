#!/usr/bin/env python3

"""
type-annotated function which takes a list of integers
and floats and returns their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list of intefers and floats
    and return the result as a float"""
    return sum(mxd_lst)
