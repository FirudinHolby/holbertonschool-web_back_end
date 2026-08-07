#!/usr/bin/env python3
'''Generators'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure time'''
    start = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    return elapsed
