from vec import Vec
from mat import Mat
from matutil import mat2rowdict, mat2coldict, rowdict2mat, coldict2mat
from matutil import listlist2mat


def dot_product_mat_vec_mult(M, v):
    '''
    >>> M = listlist2mat([[-1, 1, 2], [1, 2, 3], [2, 2, 1]])
    >>> v = Vec({0, 1, 2}, {0: 1, 1: 2, 2: 0})
    >>> dot_product_mat_vec_mult(M, v) == Vec({0, 1, 2},{0: 1, 1: 5, 2: 6})
    True
    >>> A = Mat(({'a', 'b'}, {'@', '#', '?'}),
    ... {('a', '@'): 2, ('a', '#'): 1, ('a', '?'): 3, ('b', '@'): 20,
    ... ('b', '#'): 10, ('b', '?'): 30})
    >>> b = Vec({'@', '#', '?'}, {'@': 0.5, '#': 5, '?': -1})
    >>> dot_product_mat_vec_mult(A, b) == Vec({'a', 'b'}, {'a': 3, 'b': 30.0})
    True
    '''
    assert v.D == M.D[1]
    rd = mat2rowdict(M)
    return Vec(M.D[0], {k: rd[k] * v for k in M.D[0]})


def dot_product_vec_mat_mult(v, M):
    '''
    >>> M2 = listlist2mat([[-5, 10], [-4, 8], [-3, 6], [-2, 4]])
    >>> v3 = Vec({0, 1, 2, 3}, {0: 4, 1: 3, 2: 2, 3: 1})
    >>> dot_product_vec_mat_mult(v3, M2) == Vec({0, 1},{0: -40, 1: 80})
    True
    '''
    assert v.D == M.D[0]
    cd = mat2coldict(M)
    return Vec(M.D[1], {k: v * cd[k] for k in M.D[1]})


if __name__ == '__main__':
    l = [[-1, 1, 2], [1, 2, 3], [2, 2, 1]]
    M = listlist2mat(l)
    v = Vec({0, 1, 2}, {0: 1, 1: 2, 2: 0})
    v2 = dot_product_mat_vec_mult(M, v)
    M2 = listlist2mat([[-5, 10], [-4, 8], [-3, 6], [-2, 4]])
    v3 = Vec({0, 1, 2, 3}, {0: 4, 1: 3, 2: 2, 3: 1})
    v4 = dot_product_vec_mat_mult(v3, M2)
