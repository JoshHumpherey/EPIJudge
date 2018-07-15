from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
    placeholder = ListNode()
    pointer = placeholder
    while L1 and L2:
        if L1.data < L2.data:
            pointer.next= L1
            L1 = L1.next
        else:
            pointer.next = L2
            L2 = L2.next
        pointer = pointer.next

    pointer.next = L1 or L2
    return placeholder.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
