import functools
import collections
from test_framework import generic_test


def rabin_karp(t, s):
    if len(t) == len(s) and (s == t):
        return 0
    s_len = len(s)
    substring_map = collections.defaultdict(list)
    for i in range(len(t)-s_len+1):
        slice = t[i:i+s_len]
        print(slice)
        substring_map[slice].append(i)
    places = substring_map[s]
    if len(places) > 0:
        return min(places)
    else:
        return -1


t = "GACGCCA"
s = "CGC"
test = rabin_karp(t, s)
print(test)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
