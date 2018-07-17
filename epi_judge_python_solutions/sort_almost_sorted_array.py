import heapq
import itertools

from test_framework import generic_test


def sort_approximately_sorted_array(arr, k):
    min_heap = []
    k_int = int(k)
    sequence = list(arr)
    for i in range(k_int):
        val = sequence[i]
        heapq.heappush(min_heap, val)
    result = []
    for i in range(k, len(sequence)):
        min_val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, sequence[i])
        result.append(min_val)

    while min_heap:
        min_val = heapq.heappop(min_heap)
        result.append(min_val)
    return result



def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
