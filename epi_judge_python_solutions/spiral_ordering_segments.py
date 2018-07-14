from test_framework import generic_test
test_mat = [[ 1, 2, 3, 4],
            [ 5, 6, 7, 8],
            [ 9,10,11,12],
            [13,14,15,16]]


def matrix_in_spiral_order(square_matrix):
    side_len = len(square_matrix)
    result = []
    for offset in range(1, (side_len//2)+1):
        top_row = square_matrix[offset-1]
        result.append(top_row[(offset-1):side_len-offset])
        right_col = [col[side_len-offset] for col in square_matrix]
        result.append(right_col[offset-1:side_len-offset])

        bottom_row = square_matrix[side_len-offset]
        trimmed_bottom = bottom_row[offset:side_len-offset+1]
        trimmed_bottom.reverse()
        result.append(trimmed_bottom)
        left_col = [col[offset-1] for col in square_matrix]
        trimmed_left = left_col[offset:side_len-offset]
        trimmed_left.reverse()
        result.append(trimmed_left)
        print("Count: " + str(offset))
    return result

test = matrix_in_spiral_order(test_mat)
print(test)

#if __name__ == '__main__':
#    exit(
#        generic_test.generic_test_main("spiral_ordering_segments.py",
#                                       "spiral_ordering_segments.tsv",
#                                       matrix_in_spiral_order))
