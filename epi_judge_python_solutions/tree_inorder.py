from test_framework import generic_test


def inorder_traversal(root):

    function_stack = []
    result = []
    while root or function_stack:
        if root != None:
            function_stack.append(root)
            root = root.left # Go left
        else:
            parent = function_stack.pop()
            val = parent.data
            result.append(val)  # Inorder Node
            root = parent.right   # Go Right
    return result




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
