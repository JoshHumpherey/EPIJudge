from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    if n < 2:
        return []

    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i+1):
            if i % j == 0 and i != j:
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
