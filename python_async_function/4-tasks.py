#!/usr/bin/env python3
'''New function'''


import typing
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''DEF wait_n'''
    tasks = [task_wait_random(max_delay) for i in range(n)]
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
