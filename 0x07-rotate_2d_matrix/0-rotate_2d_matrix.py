#!/usr/bin/python3
""" Rotate 2D matrix module"""


def rotate_2d_matrix(matrix):
    """
    rotate_2d_matrix - A function to rotate 2D matrix in 90 degrees
    @matrix: A 2 dimentional matrix
    Return: Nothing
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(int(i, y):
            x = (n -1 - j)
            # Current number
            tmp = matrix[i][j]
            # Change top for left
            matrix[i][j] = matrix[x][i]
            # Change left to bottom
            matrix[x][i] = matrix[y][x]
            # Change bottom to right
            matrix[y][x] = matrix[j][y]
            # Change right to top
            matrix[j][y] = tmp
