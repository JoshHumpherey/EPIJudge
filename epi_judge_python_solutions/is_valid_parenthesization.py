from test_framework import generic_test


def is_well_formed(s):
    MAPPING = {'(': ')', '{': '}', '[': ']'}
    s_list = list(s)
    stack = []
    for char in s_list:
        if char in MAPPING: # must be a left bracket
            stack.append(char)
        else: #must be a right bracket
            if len(stack) == 0:
                return False
            else:
                char_to_match = stack.pop()
                if MAPPING[char_to_match] != char:
                    return False

    if len(stack) > 0: # still unmatched brackets
        return False
    else:
        return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
