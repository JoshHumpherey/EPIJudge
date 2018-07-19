import collections
import functools
import collections
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    print(A)
    start_set = collections.defaultdict()
    end_set = collections.defaultdict()
    for event in A:
        if event.start in start_set:
            start_set[event.start] += 1
        else:
            start_set[event.start] = 1
        if event.finish in end_set:
            end_set[event.finish] += 1
        else:
            end_set[event.finish] = 1
    results = []
    current_count = 0
    for i in range(0, 24):
        if i in start_set:
            current_count += start_set[i]
        if i in end_set:
            current_count -= end_set[i]
        results.append(current_count)
    print(results)
    return max(results)


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
