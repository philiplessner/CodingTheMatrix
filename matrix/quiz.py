from mat import Mat
from vec import Vec


def identity(D):
    return Mat((D, D), {(d, d): 1 for d in D})


def mat2rowdict(A):
    return {r: Vec(A.D[1], {k[1]: v for (k, v) in A.f.items() if k[0] == r})
            for r in A.D[0]}
