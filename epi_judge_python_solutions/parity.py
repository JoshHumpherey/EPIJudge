from test_framework import generic_test


def parity(x):
    binary_list = list(str(bin(x)))
    one_count = 0
    for bit in binary_list:
        if bit == "1":
            one_count += 1
    return one_count % 2

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
