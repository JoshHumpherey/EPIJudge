import itertools

from test_framework import generic_test, test_utils

# The mapping from digit to corresponding characters.
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic(phone_number):
    master_perms = []
    partial_perms = [0] * len(phone_number)

    def recursive_helper(index):
        if index == len(phone_number):
            result = ''.join(partial_perms)
            master_perms.append(result)
        else:
            current_digit = int(phone_number[index])
            for c in MAPPING[current_digit]:
                partial_perms[index] = c
                recursive_helper(index + 1)

    recursive_helper(0)
    return master_perms


# Pythonic solution
def phone_mnemonic_pythonic(phone_number):
    return [
        ''.join(mnemonic) for mnemonic in
        itertools.product(*(MAPPING[int(digit)] for digit in phone_number))
    ]


def phone_mnemonic_pythonic_another(phone_number):
    TABLE = {
        '0': '0',
        '1': '1',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    return [
        a + b for a in TABLE.get(phone_number[:1], '')
        for b in phone_mnemonic_pythonic_another(phone_number[1:]) or ['']
    ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
