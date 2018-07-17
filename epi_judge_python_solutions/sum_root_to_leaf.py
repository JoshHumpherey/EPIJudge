from test_framework import generic_test


def sum_root_to_leaf(root, partial_path_sum=0):
    if root == None:
        return 0
    sums = []
    def dfs(root, current_string):
        current_string += str(root.data)
        if root.left == None and root.right == None:
            temp = int(current_string, 2)
            sums.append(current_string)
        else:
            if root.left != None:
                dfs(root.left, current_string)
            if root.right != None:
                dfs(root.right, current_string)
    dfs(root, "")
    total = 0
    for binary in sums:
        my_int = int(binary, 2)
        total += my_int
    return total

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
