import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(head1, head2):
    print()
    nodemap = dict()
    while (head1 != None):
        nodemap[head1.data] = head1
        head1 = head1.next
    while (head2 != None):
        if head2.data in nodemap:
            head_ref = nodemap[head2.data]
            if head_ref == head2:
                return head2
        head2 = head2.next
    return None

@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
