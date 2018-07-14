from test_framework import generic_test


def is_palindrome(s):
    str(s)
    s = s.lower()
    s_list = list(s)
    space_count = 0
    for i in range(len(s)):
        if s_list[i].isalpha() == False:
            s_list[i] = ''
            space_count += 1
    for i in range(space_count):
        s_list.remove('')
    ''.join(s_list)
    palindrome_list = list(s_list)
    print(palindrome_list)
    back = len(palindrome_list)-1
    for front in range(len(palindrome_list)//2):
        if palindrome_list[front] != palindrome_list[back]:
            return False
        back -= 1
    return True



def is_palindrome_pythonic(s):
    return all(a == b for a, b in zip(
        map(str.lower, filter(str.isalnum, s)),
        map(str.lower, filter(str.isalnum, reversed(s)))))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
