import collections

from test_framework import generic_test


def is_balanced_binary_tree(tree):
    left = dfs(tree.left, 1)
    right = dfs(tree.right, 1)
    print("FINAL === Left: " + str(left) + " and Right: " + str(right))
    if abs(left-right) <= 1:
        return True
    else:
        return False

def dfs(root, depth):
    if root == None:
        return depth
    else:
        left = dfs(root.left, depth + 1)
        right = dfs(root.right, depth + 1)
        print("Left: " + str(left) + " and Right: " + str(right))
        if abs(left-right) <= 1:
            return depth
        else:
            return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
