import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(L, pivot):
    less = []
    equal = []
    more = []
    orig = L
    while (L != None):
        val = L.data
        if val < pivot:
            less.append(val)
        elif val > pivot:
            more.append(val)
        else:
            equal.append(val)
        L = L.next
    result = less + equal + more
    i = 0
    L = orig
    while (L != None):
        L.data = result[i]
        i += 1
        L = L.next
    return orig


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
