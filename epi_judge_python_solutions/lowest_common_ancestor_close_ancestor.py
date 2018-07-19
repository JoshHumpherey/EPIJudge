import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(N1, N2):
    pointer_1 = N1
    pointer_2 = N2
    nodeset = set()
    while pointer_1 or pointer_2:
        if pointer_1:
            if pointer_1 in nodeset:
                return pointer_1
            nodeset.add(pointer_1)
            pointer_1 = pointer_1.parent
        if pointer_2:
            if pointer_2 in nodeset:
                return pointer_2
            nodeset.add(pointer_2)
            pointer_2 = pointer_2.parent
    raise ValueError('N1 and N2 are not in the same tree')


@enable_executor_hook
def lca_wrapper(executor, tree, N1, N2):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, N1),
                          must_find_node(tree, N2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
