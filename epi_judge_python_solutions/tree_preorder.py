from test_framework import generic_test


def preorder_traversal(tree):

    path = [tree]
    result = []
    while path:
        current_node = path.pop()
        if current_node != None:
            result.append(current_node.data)
            path.append(current_node.right)
            path.append(current_node.left)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
