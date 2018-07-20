from test_framework import generic_test


def is_binary_tree_bst(root, low_range=float('-inf'), high_range=float('inf')):
    if root == None:
        return True
    else:
        if root.data < low_range or root.data > high_range:
            return False
        else:
            limit = root.data
            left = is_binary_tree_bst(root.left, low_range, limit)
            right = is_binary_tree_bst(root.right, limit, high_range)
            return left and right



def is_binary_tree_bst_alternative(tree):
    def inorder_traversal(tree):
        if not tree:
            return True
        elif not inorder_traversal(tree.left):
            return False
        elif prev[0] and prev[0].data > tree.data:
            return False
        prev[0] = tree
        return inorder_traversal(tree.right)

    prev = [None]
    return inorder_traversal(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
