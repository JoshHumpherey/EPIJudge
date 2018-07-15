from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L, start, finish):
    temp = ListNode(0, L)
    pointer = temp
    values_to_reverse = []
    index = 1
    while (L != None):
        if index >= start and index <= finish:
            values_to_reverse.append(L.data)
        L = L.next
        index += 1
    values_to_reverse.reverse()
    L = temp.next
    index = 1
    counter = 0
    while (L != None):
        if index >= start and index <= finish:
            L.data = values_to_reverse[counter]
            counter += 1
        index += 1
        L = L.next
    return temp.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
