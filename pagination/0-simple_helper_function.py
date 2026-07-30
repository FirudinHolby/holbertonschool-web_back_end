#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def indef_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns page numbers to display in pagination."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
