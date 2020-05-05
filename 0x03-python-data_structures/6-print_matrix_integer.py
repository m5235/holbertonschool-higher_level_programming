#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        b = ""
        for y in range(len(matrix[x])):
            print(b, end="")
            print("{:d}".format(matrix[x][y]), end="")
            b = " "
        print()
