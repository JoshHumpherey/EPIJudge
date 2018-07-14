from test_framework import generic_test
test_mat = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
def rotate_matrix(matrix):
    n = len(matrix)-1
    for i in range(0, n):
        temp = matrix[0][i]
        matrix[0][i] = matrix[n][i]
        matrix[n][i] = matrix[n][n-i]
        matrix[n][n-i] = matrix[n-i][0]
        matrix[n-i][0] = temp
    return matrix

def print_mat(matrix):
    print("Matrix: ")
    for i in range(len(matrix)):
        print(matrix[i])
    print()

def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix

result = rotate_matrix(test_mat)
print_mat(result)
#if __name__ == '__main__':
#    exit(
#        generic_test.generic_test_main("matrix_rotation.py",
#                                       'matrix_rotation.tsv',
#                                       rotate_matrix_wrapper))
