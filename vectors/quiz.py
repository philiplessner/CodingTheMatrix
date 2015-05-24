# coding: utf-8


def addn(v, w):
    return [x + y for x, y in zip(v, w)]


def scalar_vect_mult(alpha, v):
    return [alpha * e for e in v]
