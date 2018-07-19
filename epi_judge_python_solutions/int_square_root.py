from test_framework import generic_test

def brute_square_root(k):
    results = [0]
    for i in range(k+1):
        if i*i <= k:
            results.append(i)
        else:
            break
    return results[-1]

def square_root(k):
    left = 0
    right = k
    while (left <= right):
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
