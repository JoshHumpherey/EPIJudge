import collections
import functools
import collections
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def find_smallest_subarray_covering_set(paragraph, keywords):
    if len(keywords) == len(paragraph):
        print("Returning p_low of: " + str(len(keywords)-1) + " with pair: " + str([0, len(keywords)-1]))
        return [0, len(keywords)-1]
    elif set(keywords) - set(paragraph) != set():
        return [0,0]
    hashmap = set()
    pairs = []
    for word in keywords:
        hashmap.add(word)
    keyword_amt = len(keywords)-1
    for slice_len in range(keyword_amt, len(paragraph)):
        for i in range(len(paragraph) - slice_len):
            current_slice = paragraph[i:(i+slice_len)]
            temp_set = set()
            for word in current_slice:
                temp_set.add(word)
            if hashmap - temp_set == set():
                pairs.append([i,i+slice_len])
    pair_diff = lambda x: abs(x[1]-x[0])
    min_diff = float('inf')
    min_pair = None
    if pairs == []:
        return [0,0]
    print(pairs)
    for p in pairs:
        p_low = pair_diff(p)
        print("Pair: " + str(p) + " has p_low of " + str(p_low))
        if p_low <= min_diff:
            min_diff = p_low
            min_pair = p
            if min_pair:
                min_pair[1] -= 1
    print("Returning p_low of: " + str(min_diff) + " with pair: " + str(min_pair))
    return min_pair


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
