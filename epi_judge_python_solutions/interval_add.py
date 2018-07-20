import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

class obj:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def add_interval(disjoint_intervals, new_interval):
    intervals = []
    x = obj(new_interval.left, new_interval.right)
    x_inserted = False
    for orig in disjoint_intervals:
        pair = obj(orig.left, orig.right)
        intervals.append(pair)
    result = []

    for pair in intervals:
        print("x.right: " + str(x.right + 1) + " and pair: " + str(pair.left) + "," + str(pair.right))
        if pair.left + 1 <= x.right and x.right + 1 <= pair.right:
            x.right = pair.right
            result.append(x)
        elif pair.left + 1 <= x.left and x.left + 1 <= pair.right:
            if x_inserted == False:
                x_inserted = True
                x.left = pair.left
                result.append(x)
            else:
                pop_pair = result.pop()
                pop_pair.right = pair.right
                result.append(pop_pair)

        elif x.right + 1 < pair.left:
            result.append(pair)
        elif pair.right + 1 < x.left:
            result.append(pair)
        else:
            result.append(pair)
    final = []
    for pair in result:
        final.append([pair.left, pair.right])
    return final



@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
