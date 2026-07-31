#!/usr/bin/env python3
"""Simple math utilities using variable annotations."""


def add(a: float, b: float) -> float:
    """Return the sum of two float values.

    Args:
        a (float): The first addend.
        b (float): The second addend.

    Returns:
        float: The sum of a and b.
    """
    return a + b
