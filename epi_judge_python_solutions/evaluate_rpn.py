from test_framework import generic_test


def evaluate(expression):
    print()
    intermediate_results = []
    OPERATORS = {
        '+': (lambda y, x: x + y),
        '-': (lambda y, x: x - y),
        '*': (lambda y, x: x * y),
        '/': (lambda y, x: int(x / y))
    }
    for item in expression.split(','):
        if item in OPERATORS:
            num1 = intermediate_results.pop()
            num2 = intermediate_results.pop()
            result = OPERATORS[item](int(num1), int(num2))
            intermediate_results.append(result)
        else:
            intermediate_results.append(int(item))
    print(intermediate_results)
    return intermediate_results[-1]


if __name__ == '__main__':
    exit(generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',evaluate))
