from test_framework import generic_test


def apply_permutation(perm, arr):
    perm_map = dict()
    for i in range(len(arr)):
        key = perm[i]
        value = arr[i]
        perm_map[key] = value
    result = []
    for i in range(len(arr)):
        temp = perm_map[i]
        result.append(temp)
    arr = result
    return arr


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
