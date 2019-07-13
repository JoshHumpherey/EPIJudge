from test_framework import generic_test


def parity(x):
    numOfOneBits = 0
    binaryRepresentation = bin(x)
    bString = str(binaryRepresentation)
    for i in range(2, len(binaryRepresentation)):
        bit = bString[i]
        if bit == '1':
            numOfOneBits += 1

    print(numOfOneBits)
    if numOfOneBits % 2 == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
