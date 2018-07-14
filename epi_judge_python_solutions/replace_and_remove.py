import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

test =  ["b", "d", "c", "a", "b", "a", "d", "b", "d", "b", "b", "a", "d", "c", "c", "a", "d", "a", "d",
         "d", "d", "b", "c", "c", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
def replace_and_remove(size, s):
    s_list = list(s)
    result = []
    for i in range(len(s)):
        character = s_list[i]

        if character != 'b':
            if character == 'a':
                result.append('d')
                result.append('d')
            else:
                result.append(character)
    print(result[:size-1])
    return result[:size-1]

replace_and_remove(24, test)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
