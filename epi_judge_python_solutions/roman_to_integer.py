import functools

from test_framework import generic_test

MAPPING = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_integer(s):
    if len(s) < 2:
        return MAPPING[s]
    roman_list = list(s)
    total = 0
    for i in range(len(roman_list)-1):
        key = roman_list[i]
        next_key = roman_list[i+1]
        current_num = MAPPING[key]
        next_num = MAPPING[next_key]
        if current_num < next_num:
            current_num = (current_num*-1)
            total += current_num
        elif current_num >= next_num:
            total += current_num

        if (i+1) == len(roman_list)-1:
            total += next_num
    return total





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
