import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    sorted_tasks = sorted(task_durations)
    assignments = []
    while sorted_tasks:
        min_task = sorted_tasks.pop(0)
        max_task = sorted_tasks.pop()
        assignments.append((min_task, max_task))
    return assignments




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))
