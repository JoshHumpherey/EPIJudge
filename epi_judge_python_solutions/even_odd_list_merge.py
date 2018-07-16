from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L):
    orig = L
    evens = []
    odds = []
    even = True
    while(L != None):
        if even == True:
            evens.append(L.data)
            even = False
        else:
            odds.append(L.data)
            even = True
        L = L.next

    L = orig
    result = evens + odds
    index = 0
    while (L != None):
        L.data = result[index]
        index += 1
        L = L.next
    return orig



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
