import operator
import random

from test_framework import generic_test

def find_kth_largest(k, arr):
    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr)):
        if i == len(sorted_arr)-k:
            #print("Sorted Arr: " + str(sorted_arr[i]))
            return sorted_arr[i]
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
