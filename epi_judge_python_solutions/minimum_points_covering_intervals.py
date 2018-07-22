import collections
import functools
import operator

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):
    if intervals == []:
        return 0
        
    visits = 1
    sorted_ints = sorted(intervals, key=operator.attrgetter('right'))
    visit_time = sorted_ints[0].right
    print("New visit time: " + str(visit_time))
    for i in range(1, len(sorted_ints)):
        print([sorted_ints[i].left, sorted_ints[i].right])
        if sorted_ints[i].left > visit_time:
            visits += 1
            visit_time = sorted_ints[i].right
            print("New visit time: " + str(visit_time))
    return visits



@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
