from test_framework import generic_test
import math

def buy_and_sell_stock_twice(prices):
    profits = [0]
    for divide in range(0,len(prices)):
        max1 = 0
        min1 = prices[0]
        max2 = 0
        min2 = prices[divide]
        for i1 in range(1, divide):
            if prices[i1] < min1:
                min1 = prices[i1]
            if prices[i1] - min1 > max1:
                max1 = (prices[i1] - min1)
        for i2 in range(divide, len(prices)):
            if prices[i2] < min2:
                min2 = prices[i2]
            if prices[i2]-min2 > max2:
                max2 = (prices[i2]-min2)
        profits.append(max1 + max2)
    return max(profits)



def buy_and_sell_stock_twice_constant_space(prices):
    min_prices, max_profits = [float('inf')] * 2, [0] * 2
    for price in prices:
        for i in reversed(list(range(2))):
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i],
                                price - (0 if i == 0 else max_profits[i - 1]))
    return max_profits[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
