#!/usr/bin/env python3


"""Module that defines a list of floats and integers."""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return the sum of all float and integer values in a list.
    Args:
        mxd_list (List[float, int]): The list of numbers to sum.
    Returns:
        float: The total of all values in ``mxd_list``.
    """
    sum = 0
    for i in mxd_list:
        sum += i
    return sum
