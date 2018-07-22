from test_framework import generic_test
from two_sum import has_two_sum


def has_three_sum(A, t):
    for a in A:
        result = has_two_sum(A, t-a)
        if result == True:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
