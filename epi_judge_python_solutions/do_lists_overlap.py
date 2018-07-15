import functools

from do_terminated_lists_overlap import overlapping_no_cycle_lists
from is_list_cyclic import has_cycle
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

CYCLE_LIMIT = 10000
def overlapping_lists(head1, head2):
    nodemap = dict()
    i1 = 0
    while(head1 != None):
        if i1 >= CYCLE_LIMIT:
            return None
        i1 += 1
        key = head1.data
        nodemap[key] = head1
        head1 = head1.next
    i2 = 0
    while(head2 != None):
        if i2 >= CYCLE_LIMIT:
            return None
        i2 += 1
        key = head2.data
        if key in nodemap:
            node_ref = nodemap[key]
            if node_ref == head2:
                return head2
        head2 = head2.next


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
