import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    ElementWithCachedMax = collections.namedtuple('storage',
                                                  ('element', 'max'))

    def __init__(self):
        self.storage = []
        self.my_max = 0

    def empty(self):
        if self.storage == []:
            return True
        else:
            return False

    def max(self):
        result = self.my_max
        return result

    def pop(self):
        if self.empty() == True:
            return None
        else:
            popped_val = self.storage.pop()
            if popped_val == self.my_max:
                if len(self.storage) == 0:
                    self.my_max = 0
                else:
                    self.my_max = max(self.storage)
            return popped_val

    def push(self, x):
        self.storage.append(x)
        if x > self.my_max:
            self.my_max = x



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
