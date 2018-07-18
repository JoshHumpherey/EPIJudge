import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def search_entry_equal_to_its_index(arr):
    print("Arr: " + str(arr))
    result = binary_search(arr, 0, len(arr)-1)
    return result

def binary_search(arr, start, end):
    print("Start: " + str(start) + " End: " + str(end))
    if (end < start):
        return -1
    mid = (start + end) // 2
    if arr[mid] > mid:
        return binary_search(arr, start, mid-1)
    elif arr[mid] < mid:
        return binary_search(arr, mid+1, end)
    else:
        return mid



@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(
        functools.partial(search_entry_equal_to_its_index, A))
    if result != -1:
        if A[result] != result:
            raise TestFailure("Entry does not equal to its index")
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure("There are entries which equal to its index")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_entry_equal_to_index.py",
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
