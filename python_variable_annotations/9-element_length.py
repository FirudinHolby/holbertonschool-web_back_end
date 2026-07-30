#!/usr/bin/env python3
'''STRING'''


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) \
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    '''
    Docstring for element_length
    :param lst: Description
    :type lst: typing.Iterable[typing.Sequence]
    :return: Description
    :rtype: List[Tuple[Sequence, int]]
    '''
    return [(i, len(i)) for i in lst]
