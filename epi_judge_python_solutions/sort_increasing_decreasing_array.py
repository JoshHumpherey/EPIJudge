import itertools
import heapq
from sorted_arrays_merge import merge_sorted_arrays
from test_framework import generic_test


def sort_k_increasing_decreasing_array(A):
    min_heap = []
    for element in A:
        heapq.heappush(min_heap, element)
    final = []
    while min_heap:
        final.append(heapq.heappop(min_heap))
    return final

def optimized_inc_dec(A):
    INC = []
    DEC = []
    if A[0] < A[1]:
        INC.append(A[0])
    else:
        DEC.append(A[0])

    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            INC.append(A[i])
        else:
            DEC.append(A[i])
    print(A)
    print(INC)
    print(DEC)


# Pythonic solution, uses a stateful object to trace the monotonic subarrays.
def sort_k_increasing_decreasing_array_pythonic(A):
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')

        def __call__(self, curr):
            result = curr < self._last
            self._last = curr
            return result

    return merge_sorted_arrays([
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A, Monotonic())
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_k_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
