from test_framework import generic_test


def can_reach_end(arr):
    if len(arr) < 2:
        return True
    max_advance = 0
    for i in range(len(arr)):
        if arr[i] + i > max_advance:
            max_advance = arr[i]+i
        if arr[i] == 0 and i >= max_advance:
            return False

        if max_advance >= len(arr)-1:
            return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
