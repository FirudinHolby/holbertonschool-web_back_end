#!/usr/bin/env python3

"""Module that defines a list of floats."""
from typing import List


# Defining and annotating the function
def sum_list(input_list: List[float]) -> float:
    """Return the sum of all float values in a list.

    This function accepts a list of annotated float values and returns
    their total as a single float. It is useful for demonstrating how
    typed input and output can make numeric aggregation clearer.

    Args:
        input_list (List[float]): The list of numbers to sum.

    Returns:
        float: The total of all values in ``input_list``.
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
