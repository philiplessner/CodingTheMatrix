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


def setitem(v, d, val):
    v.f[d] = val


def getitem(v, d):
    return v.f[d] if d in v.f.keys() else 0


def scalar_mul(v, alpha):
    return Vec(v.D, {d: alpha * value for d, value in v.f.items()})


def add(u, v):
    return Vec(u.D, {d: getitem(u, d) + getitem(v, d) for d in u.D})


def neg(v):
    return scalar_mul(v, -1)


def list_dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


def dot_product_list(needle, haystack):
    return [list_dot(needle, haystack[i:i+len(needle)])
            for i in range(0, len(haystack) - len(needle))]
