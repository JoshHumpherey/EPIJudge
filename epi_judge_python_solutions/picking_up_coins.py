import itertools

from test_framework import generic_test


def maximum_revenue(coins):
    print(coins)
    def find_max(a, b):
        if a > b:
            return 0

        if max_rev[a][b] == 0:
            p1 = find_max(a + 2, b)
            p2 = find_max(a + 1, b - 1)
            max_for_a = coins[a] + min(p1, p2)
            p3 = find_max(a + 1, b - 1)
            p4 = find_max(a, b - 2)
            max_for_b = coins[b] + min(p3 , p4)

            max_rev[a][b] = max(max_for_a, max_for_b)
        return max_rev[a][b]

    max_rev = [[0] * len(coins) for _ in coins]
    print(max_rev)
    result = find_max(0, len(coins) - 1)
    print(result)
    return result


def maximum_revenue_alternative(coins):
    def maximum_revenue_alternative_helper(a, b):
        if a > b:
            return 0
        elif a == b:
            return coins[a]

        if max_rev[a][b] == -1:
            max_rev[a][b] = max(
                coins[a] + prefix_sum[b] - (prefix_sum[a]
                                            if a + 1 > 0 else 0) -
                maximum_revenue_alternative_helper(a + 1, b),
                coins[b] + prefix_sum[b - 1] - (prefix_sum[a - 1]
                                                if a > 0 else 0) -
                maximum_revenue_alternative_helper(a, b - 1))
        return max_rev[a][b]

    prefix_sum = list(itertools.accumulate(coins))
    max_rev = [[-1] * len(coins) for _ in coins]
    return maximum_revenue_alternative_helper(0, len(coins) - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
