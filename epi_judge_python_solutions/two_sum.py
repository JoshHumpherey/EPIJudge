from test_framework import generic_test


def has_two_sum(A, t):
    num_map = dict()
    for x in A:
        if x in num_map:
            num_map[x] += 1
        else:
            num_map[x] = 1

    for elem in A:
        target = t - elem
        if target in num_map:
            return True
    return False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
