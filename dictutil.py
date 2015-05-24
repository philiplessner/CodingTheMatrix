# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist):
    '''
    Values in dictionary corresponding to keys in list.
    Parameters
        dct: dictionary
        keylist: list of keys
    Returns
        list of values for each key in keylist
    '''
    return [dct[e] for e in keylist]


def list2dict(L, keylist):
    '''
    Dictionary constructed from a list of values and a list of keys
    Parameters
        L: list of values
        keylist: list of keys
    Returns
    dictionary of key: value pairs
    '''
    return {k: v for k, v in zip(keylist, L)}


def listrange2dict(L):
    '''
    Dictionary of integers as keys and values from list
    Parameter
        L: list of values
    Returns
        integers as keys and L as values
    '''
    return list2dict(L, range(0, len(L)))
