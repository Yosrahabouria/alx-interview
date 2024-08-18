#!/usr/bin/python3
"""Rotate the n x n 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """def Rotate 2D matrix 90 degrees clockwise"""

    size = len(matrix)
    for layer in range(size // 2):
        first = layer
        last = size - layer - 1
        for offset in range(first, last):
            temp = matrix[first][offset]
            matrix[first][offset] = matrix[last - offset + first][first]
            matrix[last - offset + first][first] = matrix[last][last - offset + first]
            matrix[last][last - offset + first] = matrix[offset][last]
            matrix[offset][last] = temp
