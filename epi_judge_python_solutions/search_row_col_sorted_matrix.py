from test_framework import generic_test


def matrix_search(arr, target):

    row, col = 0, len(arr[0]) - 1
    # Keeps searching while there are unclassified rows and columns.
    while row < len(arr) and col >= 0:
        if arr[row][col] == target:
            return True
        elif arr[row][col] < target:
            row += 1
        else:
            col -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
