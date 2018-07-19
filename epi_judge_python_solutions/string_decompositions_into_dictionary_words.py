import collections

from test_framework import generic_test


def find_all_substrings(s, words):
    word_string = ''.join(words)
    word_len = len(word_string)
    for i in range(len(s)-word_len):
        my_slice = s[i:(i+word_len)]
        result = does_count_match(word_string, my_slice)
        if result == True:
            return [i, i+word_len]
    return False

def does_count_match(string1, string2):
    c1 = collections.Counter(string1)
    c2 = collections.Counter(string2)
    return c1 == c2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
