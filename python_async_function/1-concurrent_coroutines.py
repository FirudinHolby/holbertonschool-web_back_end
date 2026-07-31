#!/usr/bin/env python3
"""1-concurrent_coroutines

Run `n` concurrent awaits of `wait_random` from
`0-basic_async_syntax` and return their results.
"""
import asyncio
import importlib
from typing import List

# Dynamically import the helper module that provides `wait_random`.
basic_async_syntax = importlib.import_module("0-basic_async_syntax")

# Pull the function into this module's namespace for convenience.
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run `n` coroutines concurrently that await `wait_random(max_delay)`.
    """
    # 1. n sayda tapşırığı (coroutine obyektini)
    # siyahıya yığırıq (hələ ki işə düşmürlər)
    tasks = [wait_random(max_delay) for _ in range(n)]
    # 2. Ulduz (*) işarəsi ilə siyahını açırıq və
    # asyncio.gather ilə HAMISINI EYNI ANDA başladırıq
    delays = await asyncio.gather(*tasks)
    # 3. Bizdən nəticələrin artan sıra ilə qaytarılması
    # tələb olunur (ascending order)
    return sorted(delays)
