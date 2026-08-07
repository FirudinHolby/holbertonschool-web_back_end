#!/usr/bin/env python3
'''STRING'''


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    '''to kv'''
    return (k, float(v**2))
