from test_framework import generic_test


def sum_root_to_leaf(root, partial_path_sum=0):
    sum_list = []
    def dfs(root, running_total):
        if root == None:
            sum_list.append(running_total)
        else:
            running_total += str(root.data)
            dfs(root.left, running_total)
            dfs(root.right, running_total)

    dfs(root, "")
    total = 0
    for num in sum_list:
        temp = int(num, 2)
        total += temp
        print(temp)
    return total // 2



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
