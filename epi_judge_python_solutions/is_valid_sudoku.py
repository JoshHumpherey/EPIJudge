import collections
import math

from test_framework import generic_test

def is_valid_sudoku(partial_assignment):
    # ROWS
    for r in range(len(partial_assignment)):
        row_map = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for c in range(len(partial_assignment)):
            square = partial_assignment[r][c]
            if square != 0:
                if row_map[square] >= 1:
                    print_board(partial_assignment)
                    return False
                else:
                    row_map[square] += 1
    # COLUMNS
    for c in range(len(partial_assignment)):
        column_map = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for r in range(len(partial_assignment)):
            square = partial_assignment[r][c]
            if square != 0:
                if column_map[square] >= 1:
                    print_board(partial_assignment)
                    return False
                else:
                    column_map[square] += 1
    check_board(0,0,partial_assignment)
    check_board(2,0,partial_assignment)
    check_board(5,0,partial_assignment)
    check_board(2,0,partial_assignment)
    check_board(2,5,partial_assignment)
    check_board(2,5,partial_assignment)
    check_board(2,0,partial_assignment)
    check_board(5,2,partial_assignment)
    check_board(5,5,partial_assignment)
    return True

def check_board(r,c, board):
    try:
        square_map = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for r in range(r, r+2):
            for c in range(c, c+2):
                square = board[r][c]
                if square != 0:
                    if square_map[square] >= 1:
                        return False
                    else:
                        square_map[square] += 1
    except:
        print("R: " + str(r) + ", C: " + str(c))
    return True

def print_board(board):
    print()
    print("Sudoku Board: " )
    for i in range(len(board)):
        print(board[i])
    print()

# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(
        collections.Counter(k for i, row in enumerate(partial_assignment)
                            for j, c in enumerate(row) if c != 0
                            for k in ((i, str(c)), (str(c), j),
                                      (i / region_size, j / region_size,
                                       str(c)))).values(),
        default=0) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
