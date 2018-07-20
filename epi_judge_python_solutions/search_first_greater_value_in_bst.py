from test_framework import generic_test


def find_first_greater_than_k(root, k):
    subtree = root
    first_so_far = None
    while subtree:
        if subtree.data > k:
            first_so_far = subtree
            subtree = subtree.left
        else:
            subtree = subtree.right
    return first_so_far

def find_first_greater_than_k_wrapper(root, k):
    result = find_first_greater_than_k(root, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
