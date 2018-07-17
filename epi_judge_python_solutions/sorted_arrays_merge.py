import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    for array in sorted_arrays:
        for x in array:
            heapq.heappush(min_heap, x)
    result = []
    while min_heap:
        min_val = heapq.heappop(min_heap)
        result.append(min_val)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
