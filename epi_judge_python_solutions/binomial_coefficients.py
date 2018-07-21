from test_framework import generic_test
from math import factorial

def compute_binomial_coefficient(n, k):
    # (n!)/(r!(n-r)!)
    result = factorial(n)/(factorial(k)*(factorial(n-k)))
    return int(result)


def compute_binomial_coefficients_space_efficient(n, k):
    k = min(k, n - k)
    table = [1] + [0] * k
    # C(i, j) = C(i - 1, j) + C(i - 1, j - 1).
    for i in range(1, n + 1):
        for j in reversed(range(1, min(i, k) + 1)):
            table[j] = table[j] + table[j - 1]
    return table[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
