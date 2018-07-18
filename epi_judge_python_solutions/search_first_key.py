import bisect

from test_framework import generic_test


def search_first_of_k(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Pythonic solution
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
