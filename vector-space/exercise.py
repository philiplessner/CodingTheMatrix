# coding: utf-8
from vec import Vec


def vec_select(veclist, k):
    '''
    >>> D = {'a', 'b', 'c', 'd'}
    >>> v1 = Vec(D, {'a':1, 'c':3})
    >>> v2 = Vec(D, {'b':0, 'c':4})
    >>> v3 = Vec(D, {'a':2, 'b':3, 'c':0})
    >>> v4 = Vec({'d', 'a', 'b', 'c'},{})
    >>> veclist = [v1, v2, v3, v4]
    >>> vec_select(veclist, 'b') == [Vec({'a', 'c', 'd', 'b'},{'a': 1, 'c': 3}), Vec({'a', 'c', 'd', 'b'},{'c': 4, 'b': 0}), Vec({'a', 'c', 'd', 'b'},{})]
    True
    '''
    new = []
    for v in veclist:
        if k in v.f:
            if v.f[k] != 0:
                continue
            else:
                new.append(v)
        else:
            new.append(v)
    return new


def vec_sum(veclist, D):
    '''
    >>> D = {'a', 'b', 'c', 'd'}
    >>> v1 = Vec(D, {'a':1, 'c':3})
    >>> v2 = Vec(D, {'b':0, 'c':4})
    >>> v3 = Vec(D, {'a':2, 'b':3, 'c':0})
    >>> v4 = Vec({'d', 'a', 'b', 'c'},{})
    >>> veclist = [v1, v2, v3, v4]
    >>> vec_sum(veclist, D) == Vec({'a', 'c', 'd', 'b'},{'a': 3, 'c': 7, 'b': 3})
    True
    >>> veclist = []
    >>> vec_sum(veclist, D) == Vec({'a', 'c', 'd', 'b'},{})
    True
    '''
    return sum((v for v in veclist), Vec(D, {}))


def vec_select_sum(veclist, D, k):
    '''
    >>> D = {'a', 'b', 'c', 'd'}
    >>> v1 = Vec(D, {'a':1, 'c':3})
    >>> v2 = Vec(D, {'b':0, 'c':4})
    >>> v3 = Vec(D, {'a':2, 'b':3, 'c':0})
    >>> v4 = Vec({'d', 'a', 'b', 'c'},{})
    >>> veclist = [v1, v2, v3, v4]
    >>> vec_select_sum(veclist, D, 'b') == Vec({'a', 'c', 'd', 'b'},{'a': 1, 'c': 7, 'b': 0})
    True
    '''
    return vec_sum(vec_select(veclist, k), D)
