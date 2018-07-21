import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

class clock:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def knapsack(capacity, weights, values, n):
    if n == 0 or capacity == 0:
        return 0
    if capacity < weights[n-1]: # Weight exceeds capacity.. must skip
        return knapsack(capacity, weights, values, n-1)
    else:
        current_value = values[n-1]
        current_weight = weights[n-1]
        p1 = knapsack(capacity - current_weight , weights, values, n-1) + current_value
        p2 = knapsack(capacity, weights, values, n-1)
        #print("P1: " + str(p1) + ", P2: " + str(p2))
        return max(p1, p2)

def optimum_subject_to_capacity(items, capacity):
    all_clocks = []
    for x in items:
        my_clock = clock(x[1], x[0])
        all_clocks.append(my_clock)
    sorted_clocks = sorted(all_clocks, key=lambda x: x.value)
    sorted_weights = []
    sorted_vals = []
    for x in sorted_clocks:
        sorted_weights.append(x.weight)
        sorted_vals.append(x.value)
    result = knapsack(capacity, sorted_weights, sorted_vals, len(items))
    return result

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))

if __name__ == '__main__':
    exit(generic_test.generic_test_main("knapsack.py", "knapsack.tsv",optimum_subject_to_capacity_wrapper))
