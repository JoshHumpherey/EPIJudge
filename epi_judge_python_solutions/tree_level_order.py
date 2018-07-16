from test_framework import generic_test


def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result

    current_level_nodes = [tree]
    while current_level_nodes:
        level = []
        for node in current_level_nodes:
            level.append(node.data)
        result.append(level)

        next_level = []
        for node in current_level_nodes:
            if node.left != None:
                next_level.append(node.left)
            if node.right != None:
                next_level.append(node.right)
        current_level_nodes = [] #empty the queue
        for node in next_level:
            current_level_nodes.append(node)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
