from test_framework import generic_test, test_utils
import itertools

def combinations(n, k):
    orig_list = []
    for i in range(1, n+1):
        orig_list.append(i)

    result = list(itertools.permutations(orig_list, k))
    print(result)
    return result


def combinations_pythonic(n, k):
    result = [[]]
    for _ in range(k):
        result = [[i] + c for c in result
                  for i in range(1, c[0] if c else n + 1)]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
