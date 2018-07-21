import copy
import functools
import itertools
import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
EMPTY = 0
VALID = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}

def solve_sudoku(board):
    guesses = [1,2,3,4,5,6,7,8,9]
    print_board(board)
    all_valid = False

    for r in range(len(board)):
        for c in range(len(board[0])):
            val = board[r][c]
            if val == 0:
                for num in guesses:
                    board[r][c] = num
                    row = valid_row(board, r)
                    col = valid_column(board, c)
                    square = valid_square(board, r, c)
                    if row == True and col == True:
                        print("VALID")
                        break
                    elif (num == 9) and (row == False or col == False):
                        board[r][c] = 0
                        print(str([r,c]) + " is now: " + str(board[r][c]))

    print("END RESULT: " )
    print_board(board)
    return

def valid_row(board, r):
    actual = set()
    for c in range(len(board)):
        val = board[r][c]
        if val != 0 and val not in actual:
            actual.add(val)
        elif val != 0 and val in actual:
            return False
    return True

def valid_column(board, c):
    actual = set()
    for r in range(len(board[0])):
        val = board[r][c]
        if val != 0 and val not in actual:
            actual.add(val)
        elif val != 0 and val in actual:
            return False
    return True

def valid_square(board, r, c):
    if c <= 2:
        if r <= 2:
            return check_square(board, 0, 0)
        elif r > 2 and r <= 5:
            return check_square(board, 3, 0)
        else:
            return check_square(board, 6, 0)
    elif c > 2 and c <= 5:
        if r <= 2:
            return check_square(board, 0, 3)
        elif r > 2 and r <= 5:
            return check_square(board, 3, 3)
        else:
            return check_square(board, 6, 3)
    else:
        if r <= 2:
            return check_square(board, 0, 6)
        elif r > 2 and r <= 5:
            return check_square(board, 3, 6)
        else:
            return check_square(board, 6, 6)

def check_square(board, r, c):
    actual = set()
    for i in range(r, r + 3):
        for j in range(c, c+3):
            val = board[i][j]
            if val != 0 and val not in actual:
                actual.add(val)
            elif val != 0 and val in actual:
                return False
    return True

def print_board(board):
    print("Sudoku Matrix:  ")
    for r in range(len(board)):
        print(board[r])
    print()

def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)

def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]

@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))

    for i in range(len(solved)):
        assert_unique_seq(solved[i])
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))

TEST = [[0, 3, 2, 0, 0, 0, 8, 0, 4],
        [8, 0, 0, 2, 0, 0, 0, 7, 0],
        [0, 1, 7, 0, 0, 5, 9, 0, 6],
        [5, 8, 0, 0, 2, 0, 0, 3, 0],
        [0, 0, 6, 0, 4, 0, 7, 0, 0],
        [0, 0, 4, 9, 1, 3, 0, 6, 0],
        [0, 0, 0, 7, 3, 0, 2, 0, 0],
        [0, 5, 9, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 8, 0, 9, 0, 0, 0]]

#solve_sudoku(TEST)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("sudoku_solve.py", 'sudoku_solve.tsv', solve_sudoku_wrapper))
