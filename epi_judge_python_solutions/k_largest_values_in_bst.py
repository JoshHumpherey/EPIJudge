from test_framework import generic_test, test_utils


def find_k_largest_in_bst(root, k):
    node_list = []
    def pre_order(root):
        if root == None:
            return
        else:
            node_list.append(root.data)
            pre_order(root.left)
            pre_order(root.right)
    pre_order(root)
    sorted_data = sorted(node_list)
    return sorted_data[(len(sorted_data)-k):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
