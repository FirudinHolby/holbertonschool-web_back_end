#!/usr/bin/env python3
'''Generators'''


import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''Comprehension'''
    result = [i async for i in async_generator()]
    return result
