import collections
import heapq
from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    def __init__(self):
        self.storage = []
        self.my_max = float('-inf')
        self.heapmap = dict()
        self.id_count = 100000000

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
        key = heapq.heappop(self.storage)
        val = self.heapmap[key]
        self.heapmap.pop(key, val)
        if val == self.my_max:
            self.my_max = self.find_map_max()
        return val

    def find_map_max(self):
        best_max = float('-inf')
        for key in self.heapmap:
            if self.heapmap[key] > best_max:
                best_max = self.heapmap[key]
        return best_max

    def push(self, x):
        if x > self.my_max:
            self.my_max = x
        key = self.id_count
        self.heapmap[key] = x
        heapq.heappush(self.storage, key)
        #print(self.heapmap)
        self.id_count -= 1




my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

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
