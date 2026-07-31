#!/usr/bin/env python3
"""Simple conversion utilities using variable annotations."""


def to_str(a: float) -> str:
    """Return the string representation of the input.

    The function accepts a value annotated as a float and returns its
    string form using the built-in `str()` conversion. Annotations help
    with readability and static type checking.

    Args:
        a (float): The value to convert to a string.

    Returns:
        str: The string representation of `a`.
    """
    return str(a)
