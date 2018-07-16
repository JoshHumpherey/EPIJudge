from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    orig = L
    values = []
    while (L != None):
        value = L.data
        values.append(value)
        L = L.next
    total = len(values)
    shifted_vals = values[total-k:] + values[:(total-k)]
    print(shifted_vals)
    L = orig
    i = 0
    while (L != None):
        L.data = shifted_vals[i]
        i += 1
        L = L.next
    return orig





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
