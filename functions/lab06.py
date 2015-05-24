# coding: utf-8
from dictutil import dict2list


def read_file(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        return [line for line in f]


def makeInverseIndex(strlist):
    '''
    Dictionary where each word is a key
    and values is the set of indexes of the strings it appears in.
    Parameters
        strlist: list of strings
    Returns
        inverseIndex: dictionary with words as keys
        and indexes of strings in strlist where the word
        appears as values (values are in a set)
    '''
    inverseIndex = {}
    removed_newlines = [e.strip() for e in strlist]
    words = [set(e.split()) for e in removed_newlines]
    for i, ws in enumerate(words):
        for w in ws:
            if w not in inverseIndex.keys():
                inverseIndex[w] = set([i])
            else:
                inverseIndex[w].add(i)
    return inverseIndex


def orSearch(inverseIndex, query):
    '''
    Find documents that contain any words in the query list.
    Parameters
        inverseIndex:  dictionary with words as keys
        and indexes of strings in strlist where the word
        appears as values (values are in a set)
        query: list of words
    Returns
        S: set of document indexes containing any of the words
    '''
    S = set()
    docs = dict2list(inverseIndex, query)
    for e in docs:
        S.update(e)
    return S


def andSearch(inverseIndex, query):
    '''
    Find documents that contain all words in the query list.
    Parameters
        inverseIndex:  dictionary with words as keys
        and indexes of strings in strlist where the word
        appears as values (values are in a set)
        query: list of words
    Returns
        S: set of document indexes containing all of the words
    '''
    docs = dict2list(inverseIndex, query)
    for i, e in enumerate(docs):
        if i == 0:
            S = set(e)
        else:
            S.intersection_update(e)
    return S
