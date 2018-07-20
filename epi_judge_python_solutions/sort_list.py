from list_node import ListNode
from test_framework import generic_test

def stable_sort_list(list_node):

    if not list_node or not list_node.next:
        return list_node

    # Find the midpoint of list_node using a slow and a fast pointer.
    pre_slow = None
    slow = list_node
    fast = list_node

    while fast and fast.next:
        pre_slow = slow
        fast = fast.next.next
        slow = slow.next
    pre_slow.next = None  # Splits the list into two equal-sized lists.
    print("Merge sort with endpoints: " + str(list_node.data) + " and " + str(slow.data))
    return merge_two_sorted_lists(stable_sort_list(list_node), stable_sort_list(slow))

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
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
