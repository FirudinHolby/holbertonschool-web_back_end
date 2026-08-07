#!/usr/bin/env python3
'''Generators'''


import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    '''Loop for yield'''
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
