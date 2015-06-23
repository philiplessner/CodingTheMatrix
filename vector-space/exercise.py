def vec_select(veclist, k):
    '''
    >>> from vec import Vec
    >>> D = {'a', 'b', 'c', 'd'}
    >>> v1 = Vec(D, {'a':1, 'c':3})
    >>> v2 = Vec(D, {'b':0, 'c':4})
    >>> v3 = Vec(D, {'a':2, 'b':3, 'c':0})
    >>> veclist = [v1, v2, v3]
    >>> vec_select(veclist, 'b') == [Vec({'d', 'a', 'b', 'c'},{'a': 1, 'c': 3}), Vec({'d', 'a', 'b', 'c'},{'b': 0, 'c': 4})]
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
