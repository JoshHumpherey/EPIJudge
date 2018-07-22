import functools

from test_framework import generic_test


def minimum_path_weight(triangle):
    print_triangle(triangle)
    def gen_paths(triangle, sum, index, current_col):
        if index == len(triangle):
            return sum
        else:
            left = gen_paths(triangle, sum + triangle[index][current_col], index + 1, current_col)
            right = gen_paths(triangle, sum + triangle[index][current_col], index + 1, current_col+1)
            return min(left, right)


    optimal_sum = gen_paths(triangle, 0, 0, 0)
    return optimal_sum


def print_triangle(tri):
    print("Triangle: " )
    for r in range(len(tri)):
        print(tri[r])
    print()
def minimum_path_weight_pythonic(triangle):
    return min(functools.reduce(lambda result, tri: [r + min(a, b) for r, a, b in zip(tri, [float('inf')] + result, result + [float('inf')])], triangle, [0]))

if __name__ == '__main__':
    exit(generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
