from test_framework import generic_test


def is_symmetric(root):
    start_list = [root.data]
    left_list = construct_list(root.left, start_list, True)
    right_list = construct_list(root.right, start_list, False)
    print("Left list: " + str(left_list))
    print("Right list: " + str(right_list))
    return left_list == right_list

def construct_list(root, storage, is_left):
    if root == None:
        return storage
    else:
        current_val = root.data
        if is_left == True:
            left1 = construct_list(root.left, [current_val], True)
            right1 = construct_list(root.right, [current_val], True)
            return storage + left1 + right1
        else:
            right2 = construct_list(root.right, [current_val], False)
            left2 = construct_list(root.left, [current_val], False)
            return storage + right2 + left2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
