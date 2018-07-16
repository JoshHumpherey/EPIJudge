import collections
import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, N1, N2):
    common_ancestors = [tree]
    print("ROOT: " + str(tree.data))
    partial = [tree]
    while partial:
        node = partial.pop()
        left_side = dfs(node.left, N1, N2)
        right_side = dfs(node.right, N1, N2)
        print("Left side: " + str(left_side) + " Right side: " + str(right_side))
        if left_side != False:
            if node.left != N1 and node.left != N2:
                common_ancestors.append(node.left)
                partial.append(node.left)
            print("Adding to partial: " + str(node.data))
        if right_side != False:
            if node.right != N1 and node.right != N2:
                common_ancestors.append(node.right)
                partial.append(node.right)
            print("Adding to partial: " + str(node.data))

    return common_ancestors[-1]

def dfs(root, N1, N2):
    if root == None:
        return False
    if root == N1 or root == N2:
        return True

    left = dfs(root.left, N1, N2)
    right = dfs(root.right, N1, N2)
    return left == right


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
