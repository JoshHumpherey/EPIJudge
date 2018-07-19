from test_framework import generic_test


def longest_subarray_with_distinct_entries(arr):
    if len(arr) < 1:
        return 0
    longest_count = 1
    for i in range(len(arr)):
        hash_set = set()
        for j in range(i, len(arr)):
            if arr[j] in hash_set:
                if len(hash_set) > longest_count:
                    longest_count = len(hash_set)
                break
            else:
                hash_set.add(arr[j])
                if j == len(arr)-1:
                    if len(hash_set) > longest_count:
                        longest_count = len(hash_set)
    return longest_count

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
