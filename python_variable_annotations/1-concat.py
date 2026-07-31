#!/usr/bin/env python3
"""Simple string utilities using variable annotations."""


def concat(a: str, b: str) -> str:
    """Return the concatenation of two strings.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return a + b
