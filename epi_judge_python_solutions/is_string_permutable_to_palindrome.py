import collections

from test_framework import generic_test


def can_form_palindrome(s):
    print(s)
    s_list = list(s)
    is_odd = False
    c1 = collections.Counter(s_list)
    for key in c1:
        val = c1[key]
        if val % 2 == 1:
            if is_odd == False:
                is_odd = True
            else:
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
