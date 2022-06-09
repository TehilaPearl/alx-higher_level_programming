#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    i = 0
    j = 1

    squared_matrix = [list(map(lambda j: j ** 2, i)) for i in matrix]
    return squared_matrix
