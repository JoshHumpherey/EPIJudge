from test_framework import generic_test
import math

def next_permutation(perm):
    min_point = 0
    diff = math.inf
    diff_point = None
    all_decreasing = True
    for i in range(1, len(perm)):
        if perm[i] >= perm[i-1]:
            min_point = i-1
            all_decreasing = False
            break
    if all_decreasing == True:
        return perm
    for i in range(min_point + 1, len(perm)):
        if perm[i] - perm[min_point] < diff:
            diff = perm[i] - perm[min_point]
            diff_point = i
    temp = perm[min_point]
    perm[min_point] = perm[diff_point]
    perm[diff_point] = temp
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
