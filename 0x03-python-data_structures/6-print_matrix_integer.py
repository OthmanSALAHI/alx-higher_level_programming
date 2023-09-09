#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return

    columnSize = 0
    rowSize = len(matrix)
    for row in range(rowSize):
        columnSize = len(matrix[row])
        for col in range(columnSize):
            print("{:d}".format(matrix[row][col]), end="")
            if col == columnSize - 1:
                print()
                break
            print(" ", end="")