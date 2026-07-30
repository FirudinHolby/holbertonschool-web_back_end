#!/usr/bin/env python3
'''Measure runtime'''


from concurrent_coroutines import wait_n
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    '''Return runtime of function'''
    async def _measure():
        start = time.perf_counter()
        await wait_n(n, max_delay)
        elapsed = time.perf_counter() - start
        return elapsed / n

    return asyncio.run(_measure())