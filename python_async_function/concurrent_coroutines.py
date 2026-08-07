#!/usr/bin/env python3
'''ASYNC concurrent coroutines'''


from basic_async_syntax import wait_random
import asyncio
import typing


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''DEF wait_n'''
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    result = []
    for delay in delays:
        inserted = False
        for j in range(len(result)):
            if delay < result[j]:
                result.insert(j, delay)
                inserted = True
                break
        if not inserted:
            result.append(delay)
    return result
