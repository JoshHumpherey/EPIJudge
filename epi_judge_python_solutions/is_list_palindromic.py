from reverse_linked_list_iterative import reverse_linked_list
from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    data_list = []
    orig = L
    while L:
        data_list.append(L.data)
        L = L.next
    end = len(data_list)-1
    for start in range(len(data_list)//2):
        if data_list[start] != data_list[end]:
            return False
        end -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
