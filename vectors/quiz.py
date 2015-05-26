# coding: utf-8
from vec import Vec


def addn(v, w):
    return [x + y for x, y in zip(v, w)]


def scalar_vect_mult(alpha, v):
    return [alpha * e for e in v]


def segment(pt1, pt2):
    return [addn(scalar_vect_mult(i / 100.,  pt1),
                 scalar_vect_mult(1. - i / 100., pt2))
            for i in range(0, 101)]


def zero_vec(D):
    return Vec(D, {d: 0 for d in D})
