from test_framework import generic_test


def majority_search(stream):
    the_stream = []
    for x in stream:
        the_stream.append(x)
    maj_element = None
    maj_count = 0
    for i in range(len(the_stream)):
        if the_stream[i] == maj_element:
            maj_count += 1
        else:
            maj_count -= 1
            if maj_count < 1:
                maj_element = the_stream[i]
                maj_count = 1
    print(maj_element)
    return maj_element


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
