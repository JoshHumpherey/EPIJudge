import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    class StackObj():
        def __init__(self, order, data):
            self.order = order
            self.data = data

    def __init__(self):
        self.storage = []
        self.my_max = float('-inf')

    def empty(self):
        if len(self.storage) == 0:
            return True
        else:
            return False

    def max(self):
        if self.empty != True:
            return self.my_max
        else:
            return Exception('Empty Stack has no max!')

    def pop(self):
        fresh_val = heaqp.heappop(self.storage)
        if fresh_val == my_max and len(self.storage) > 0:
            self.my_max = heapq.heappop(self.storage).data

    def push(self, x):
        if x > self.my_max:
            my_max.self = x
        self.increase_time()
        my_data = StackObj(0, x)
        heapq.heappush(self.storage, my_data)

    def increase_time():
        for obj in self.storage:
            obj.order += 1



def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
