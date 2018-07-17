import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(N1, N2):
    nodemap = {N1.data:N1,N2.data:N2}
    while N1.parent or N2.parent:
        if N1.parent.data in nodemap:
            return N1.parent
        else:
            nodemap[N1.parent.data] = N1.parent
        if N2.parent.data in nodemap:
            return N2.parent
        else:
            nodemap[N2.parent.data] = N2.parent
        N1 = (N1.parent if not N1 else None)
        N2 = (N2.parent if not N2 else None)
    return N1





@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
