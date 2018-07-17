from test_framework import generic_test


class Queue:
    def __init__(self):
        self.main_stack = []
        self.buffer_stack = []

    def enqueue(self, x):
        if self.main_stack == []:
            self.main_stack.append(x)
        else:
            for i in range(len(self.main_stack)):
                temp = self.main_stack.pop()
                self.buffer_stack.append(temp)
            self.main_stack.append(x)
            for i in range(len(self.buffer_stack)):
                temp = self.buffer_stack.pop()
                self.main_stack.append(temp)

    def dequeue(self):
        if self.main_stack == []:
            return None
        else:
            return self.main_stack.pop()



def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
