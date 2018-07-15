from list_node import ListNode
from test_framework import generic_test

def remove_kth_last(L, k):
    temp = ListNode(0, L)
    fast_pointer = slow_pointer = temp.next
    slow_count = 1
    fast_count = 2
    while (fast_pointer.next.next != None):
        slow_pointer = slow_pointer.next
        slow_count += 1
        fast_pointer = fast_pointer.next.next
        fast_count += 2
    print("Fast: " + str(fast_count) + ", Slow: " + str(slow_count))
    target_val = fast_count - k + 1
    while (slow_pointer != None):
        if slow_count == target_val:
            slow_pointer.data = slow_pointer.next.data
            slow_pointer.next = slow_pointer.next.next
            return temp.next
        slow_count += 1
        slow_pointer = slow_pointer.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
