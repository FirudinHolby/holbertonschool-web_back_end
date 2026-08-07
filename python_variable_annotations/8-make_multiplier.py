#!/usr/bin/env python3
'''STRING'''


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''make multiplier'''
    def multiplier_func(number: float) -> float:
        '''multiplier func'''
        return number * multiplier
    return multiplier_func
