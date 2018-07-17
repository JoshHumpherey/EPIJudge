from test_framework import generic_test


def has_path_sum(root, remaining_weight):
    def dfs(root, target, current_sum):
        if root.left == None and root.right == None:
            current_sum += root.data
            if target == current_sum:
                return True
        else:
            right = False
            left = False
            current_sum += root.data
            if root.left:
                left = dfs(root.left, target, current_sum)
            if root.right:
                right = dfs(root.right, target, current_sum)
            return left or right

    if dfs(root, remaining_weight, 0) == True:
        return True
    else:
        return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
