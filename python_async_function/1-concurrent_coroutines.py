#!/usr/bin/env python3
"""sdfsdfdsfsd"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """sdfds"""
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []
    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
