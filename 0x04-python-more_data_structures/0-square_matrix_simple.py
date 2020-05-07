#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        for i in matrix:
            new_matrix.append(list(map(lambda y: y**2, i)))
        return new_matrix
