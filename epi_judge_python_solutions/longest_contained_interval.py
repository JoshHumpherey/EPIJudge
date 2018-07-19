from test_framework import generic_test


def longest_contained_range(arr):
    hash_set = set()
    for i in range(len(arr)):
        hash_set.add(arr[i])
    longest_range = 1
    for i in range(len(arr)):
        temp_count = 0
        current_num = arr[i]
        while(True):
            if current_num in hash_set:
                temp_count += 1
                current_num += 1
            else:
                if temp_count > longest_range:
                    longest_range = temp_count
                break
    return longest_range



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
