from test_framework import generic_test

cache = {}


def fibonacci(n):
    fibmap = dict()
    fibmap[0] = 0
    fibmap[1] = 1
    if n <= 1:
        return fibmap[n]
    else:
        counter = 2
        while (counter <= n):
            fibmap[counter] = fibmap[counter-1]+fibmap[counter-2]
            counter += 1
    return fibmap[n]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
