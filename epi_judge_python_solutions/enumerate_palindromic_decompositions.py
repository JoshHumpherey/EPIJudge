from test_framework import generic_test


def palindrome_decompositions(input):
    result = []
    def gen_decomp(index, partial_partition):
        if index == len(input):
            result.append(list(partial_partition))
            return

        for i in range(index + 1, len(input) + 1):
            prefix = input[index:i]
            print("Prefix: " + str(prefix))
            if prefix == prefix[::-1]: # reverses list
                gen_decomp(i, partial_partition + [prefix])


    gen_decomp(0, [])
    print(result)
    return result


# Pythonic solution uses bottom-up construction.
def palindrome_decompositions_pythonic(text):
    return ([[text[:i]] + right for i in range(1,
                                               len(text) + 1)
             if text[:i] == text[:i][::-1]
             for right in palindrome_decompositions_pythonic(text[i:])]
            or [[]])


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
