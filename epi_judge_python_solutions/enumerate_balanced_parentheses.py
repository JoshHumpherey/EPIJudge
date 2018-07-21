from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    result = []
    def gen_combos(left_needed, right_needed, valid_prefix):
        if left_needed > 0:
            gen_combos(left_needed-1, right_needed, valid_prefix + '(')
        if left_needed < right_needed:
            gen_combos(left_needed, right_needed-1, valid_prefix + ')')
        if right_needed == 0:
            result.append(valid_prefix)
    gen_combos(num_pairs, num_pairs, '')
    print(result)
    return result


def generate_balanced_parentheses_pythonic(num_pairs, num_left_open=0):
    if not num_pairs:
        return [')' * num_left_open]
    if not num_left_open:
        return [
            '(' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open + 1)
        ]
    else:
        return ([
            '(' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open + 1)
        ] + [
            ')' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open - 1)
        ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
