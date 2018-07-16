from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class QueueWithMax:
    def __init__(self):
        self.storage = deque()
        self.my_max = -10000000000000000000000000000000000000000000000000000000000

    def enqueue(self, x):
        if x > self.my_max:
            self.my_max = x
        self.storage.append(x)

    def dequeue(self):
        if len(self.storage) == 0:
            return IndexError("Queue is empty!")
        else:
            pop_val = self.storage.popleft()
            if pop_val == self.my_max:
                if len(self.storage) != 0:
                    self.my_max = max(self.storage)
            return pop_val

    def max(self):
        if len(self.storage) == 0:
            return IndexError('Queue is empty!')
        else:
            return self.my_max

myq = QueueWithMax()
myq.enqueue(1)
myq.enqueue(2)
myq.enqueue(3)
print(myq.max())
val = myq.dequeue()
print("Returned val: " + str(val))
print(myq.max())

def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
                    print('\n')
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
                    print('\n')
            else:
                raise RuntimeError("Unsupported queue operation: " + op)

    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
