import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(coded_string):
    coded_len = len(coded_string)
    coded_list = list(coded_string)
    decoded_list = []
    current_num = []
    current_char = coded_string[0]
    for i in range(1, coded_len):
        s = coded_list[i]
        if s.isnumeric():
            current_num.append(s)
            if coded_len-1 == i:
                my_base = ''.join(current_num)
                my_int = int(my_base)
                for j in range(my_int):
                    decoded_list.append(current_char)

        if s.isalpha():
            my_base = ''.join(current_num)
            my_int = int(my_base)
            for j in range(my_int):
                decoded_list.append(current_char)
            current_num = []
            current_char = s
    final = ''.join(decoded_list)
    print("FINAL: " + str(final))
    return final

def encoding(plain_string):
    encoded_list = []
    decoded_list = list(plain_string)
    last_char = decoded_list[0]
    repeat_count = 1
    for i in range(1, len(decoded_list)):
        char = decoded_list[i]
        if char == last_char:
            repeat_count += 1
        else:
            encoding = last_char + str(repeat_count)
            encoded_list.append(encoding)
            last_char = char
            repeat_count = 1

        if len(decoded_list)-1 == i:
            encoding = char + str(repeat_count)
            encoded_list.append(encoding)
    return ''.join(encoded_list)

test_str = "abcccbba"
secret = encoding(test_str)
print("Encoded String: " + str(secret))
decrypted = decoding(secret)
print("Decoded String: " + str(decrypted))

def encoding_pythonic(s):
    return ''.join(str(len(list(g))) + c for c, g in itertools.groupby(s))


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
