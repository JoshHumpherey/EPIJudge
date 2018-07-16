from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self._entries = [None] * capacity * 100
        self.capacity = capacity
        self.current_count = 0

    def enqueue(self, x):
        print("Queing " + str(x) + " to index: " + str(self.current_count))
        self._entries[self.current_count] = x
        self.current_count += 1



    def dequeue(self):
        if (self.current_count == 0):
            return None

        self.current_count -= 1
        return self._entries.pop(0)

    def size(self):
        return self.current_count


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
