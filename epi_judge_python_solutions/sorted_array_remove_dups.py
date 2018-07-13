import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(arr):
    if not arr:
        return 0
    total = len(arr)
    deletions = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            deletions += 1
    result = total - deletions
    print(result)
    return result


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
