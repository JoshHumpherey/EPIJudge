from test_framework import generic_test


def test_collatz_conjecture(n):
    verified_numbers = set()
    verified_numbers.add(1)
    verified_numbers.add(2)
    for i in range(3, n + 1):
        current_test = set()
        current_num = i
        while(current_num <= 1):
            if current_num == 1:
                verified_numbers.add(i)
                break
            elif current_num in verified_numbers:
                break
            elif current_num in current_test:
                break
            elif current_num % 2 == 1:
                current_num = (3 * current_test) + 1
                current_test.add(current_num)
            else:
                current_num = current_num // 2
                current_test.add(current_num)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("collatz_checker.py",
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
