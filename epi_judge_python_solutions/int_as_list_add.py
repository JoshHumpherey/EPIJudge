from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1, L2):
    orig = ListNode()
    pointer = orig
    carry = 0

    while L1 or L2 or carry:
        sum = (L1.data if L1 else 0) + (L2.data if L2 else 0) + carry
        L1 = (L1.next if L1 else None)
        L2 = (L2.next if L2 else None)
        pointer.next = ListNode(sum % 10)
        carry = sum // 10
        pointer = pointer.next
    return orig.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
