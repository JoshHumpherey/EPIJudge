from test_framework import generic_test
import math

def buy_and_sell_stock_once(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        sell_today = prices[i]-min_price
        if sell_today > max_profit:
            max_profit = sell_today
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
