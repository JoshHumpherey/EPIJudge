import math

from test_framework import generic_test, test_utils


def create_power_set(input_set):
    print("Input Set: " + str(input_set))
    power_set = []
    def generate_power_set(index, already_selected):
        if index == len(input_set):
            power_set.append(list(already_selected))
            return
        else:
            # makes sure empty set exists and all other numbers
            generate_power_set(index + 1, already_selected)
            # This creates the subsets
            generate_power_set(index + 1, already_selected + [input_set[index]])
    generate_power_set(0, [])
    return power_set

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       create_power_set,
                                       test_utils.unordered_compare))
