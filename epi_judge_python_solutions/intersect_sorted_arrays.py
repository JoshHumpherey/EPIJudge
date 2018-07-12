from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    results = []
    mappingA = dict()
    mappingB = dict()
    for i in range(len(A)):
        key = A[i]
        if A[i] not in mappingA:
            mappingA[key] = key
    for i in range(len(B)):
        key = B[i]
        if B[i] not in mappingB:
            mappingB[key] = key
    for key in mappingA:
        if key in mappingB:
            results.append(key)
    return results




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
