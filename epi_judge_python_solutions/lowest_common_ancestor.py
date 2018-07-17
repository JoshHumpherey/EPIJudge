import collections
import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(root, N1, N2):
    common_nodes = []
    queue = [root]

    def dfs(root, target):
        left = False
        right = False
        if root == None:
            return False
        if root == target:
            return True
        if root.left != None:
            left = dfs(root.left, target)
        if root.right != None:
            right = dfs(root.right, target)
        return left or right


    while queue:
        for node in queue:
            target1 = dfs(node, N1)
            target2 = dfs(node, N2)
            if (target1 and target2):
                common_nodes.append(node)
        temp = []
        for node in queue:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp
    return common_nodes[-1]


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
