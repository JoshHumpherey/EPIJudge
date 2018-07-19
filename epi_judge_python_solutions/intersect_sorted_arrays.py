from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    hashset = set()
    for element in A:
        hashset.add(element)
    result_set = set()
    for element in B:
        if element in hashset:
            result_set.add(element)
    unique_results = []
    for unique in result_set:
        unique_results.append(unique)
    final = sorted(unique_results)
    return final



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
