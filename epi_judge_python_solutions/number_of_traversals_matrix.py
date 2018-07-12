import itertools
import numpy as np
from test_framework import generic_test


def number_of_ways(r, c):
    value_grid = np.zeros((r,c))
    for i in range(r):
        value_grid[i][0] = 1
    for i in range(c):
        value_grid[0][i] = 1
    for row in range(1, r):
        for col in range(1, c):
            value_grid[row][col] = value_grid[row-1][col] + value_grid[row][col-1]
    return value_grid[r-1][c-1]




def compute_number_of_ways_space_efficient(n, m):
    if n < m:
        n, m = m, n

    A = [1] * m
    for i in range(1, n):
        prev_res = 0
        for j in range(m):
            A[j] += prev_res
            prev_res = A[j]
    return A[m - 1]


# Pythonic implementation of space efficient solution.
def number_of_ways_pythonic(n, m):
    if n < m:
        n, m = m, n

    A = [1] * m
    for _ in range(1, n):
        A = list(itertools.accumulate(A))
    return A[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
