#!/usr/bin/env python3
"""Simple math utilities using variable annotations."""


def floor(a: float) -> int:
    """Return the floor of a float as an integer.

    This function converts a float to an integer by truncating towards zero
    using the built-in `int()` conversion. It is annotated to accept a
    float and return an int for clarity and static type checking.

    Args:
        a (float): The number to convert.

    Returns:
        int: The integer representation of `a`.
    """
    if a < 0:
        return int(a) - 1
    return int(a)
