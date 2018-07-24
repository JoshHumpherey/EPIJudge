from test_framework import generic_test


def parity(x):
    one_count = 0
    bin_num = str(bin(x))
    for i in range(len(bin_num)):
        if bin_num[i] == '1':
            one_count += 1
    if one_count % 2 == 1:
        return True
    else:
        return False
if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
