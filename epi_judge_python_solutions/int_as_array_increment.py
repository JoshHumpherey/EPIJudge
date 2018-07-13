from test_framework import generic_test


def plus_one(A):
    string_A = ""
    for i in range(len(A)):
        string_A += str(A[i])
    int_A = int(string_A)
    int_B = str(int_A + 1)
    result = []
    string_B = list(int_B)
    for i in range(len(string_B)):
        temp = string_B[i]
        result.append(int(temp))
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
