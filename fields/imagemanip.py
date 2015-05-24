# coding: utf-8
from image import file2image


def read_image(filepath):
    return file2image(filepath)


def base_image(data):
    return [k + (len(data) - i) * (0 + 1j)
            for i, y in enumerate(data) for k, x in enumerate(y) if x[0] < 120]


def f(z):
    xmax = max(w.real for w in z)
    ymax = max(w.imag for w in z)
    return [w - (xmax / 2. + (ymax / 2.)*(0+1j)) for w in z]
