from vec import Vec
from mat import Mat
from matutil import mat2rowdict, mat2coldict, rowdict2mat, coldict2mat
from matutil import listlist2mat


def lin_comb_mat_vec_mult(M, v):
    assert v.D == M.D[1]
    rd = mat2rowdict(M)
    return Vec(M.D[0], {k: rd[k] * v for k in v.D})


if __name__ == '__main__':
    l = [[-1, 1, 2], [1, 2, 3], [2, 2, 1]]
    M = listlist2mat(l)
    v = Vec({0, 1, 2}, {0: 1, 1: 2, 2: 0})
    v2 = lin_comb_mat_vec_mult(M, v)
