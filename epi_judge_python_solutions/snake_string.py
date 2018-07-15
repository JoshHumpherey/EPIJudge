from test_framework import generic_test


def snake_string(s):
    EDGE = 4
    MID = 2
    char_list = list(s)
    list_len = len(char_list)
    if list_len == 1:
        return s
    if list_len == 2:
        char_list.reverse()
        return ''.join(char_list)
    top = 1
    mid = 0
    bot = 3
    top_list = []
    mid_list = []
    bot_list = []
    for i in range(list_len):
        char = char_list[i]
        if i == top:
            top_list.append(char)
            top += EDGE
        if i == mid:
            mid_list.append(char)
            mid += MID
        if i == bot:
            bot_list.append(char)
            bot += EDGE
    result = top_list + mid_list + bot_list
    return ''.join(result)




# Python solution uses slicing with right steps.
def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
