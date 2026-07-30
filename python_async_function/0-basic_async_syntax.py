#!/usr/bin/env python3
'''ASYNC'''


import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    '''Coroutine'''
    start = time.perf_counter()
    await asyncio.sleep(random.uniform(0, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed
