#!/usr/bin/env python3

"""
Given parameters and the return value, add type
annotations to the function
"""


from typing import Mapping, Any, TypeVar, Union


# Define a generic type variable for the default value
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Get a value from a dictionary safely

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Optional[T], optional): The default value to
            return if the key is not found. Default is None.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        otherwise the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
