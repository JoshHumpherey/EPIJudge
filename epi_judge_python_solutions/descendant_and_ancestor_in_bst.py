import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(N1, N2, mid_node):
    if N1 == N2:
        return False
    n1_ancestor = dfs(N1, mid_node)
    n2_ancestor = dfs(N2, mid_node)
    if n1_ancestor and not n2_ancestor:
        n2_child = dfs(mid_node, N2)
        return n2_child
    elif n2_ancestor and not n1_ancestor:
        n1_child = dfs(mid_node, N1)
        return n1_child
    else:
        return False

def dfs(root, target):
    if root == None:
        return False
    if root == target:
        return True
    left = dfs(root.left, target)
    right = dfs(root.right, target)
    return left or right


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
        executor, tree, possible_anc_or_desc_0, possible_anc_or_desc_1,
        middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
