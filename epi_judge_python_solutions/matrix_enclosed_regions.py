import collections
import time
from test_framework import generic_test
import numpy as np


def fill_surrounded_regions(board):
    VISITED_MAP = np.zeros((len(board), len(board[0])))
    print_board(board)
    CHECK = 'W'
    FILL = 'B'
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == CHECK:
                dfs(board, r, c, VISITED_MAP)
    print_board(board)
    return board



def dfs(board, r, c, VISITED_MAP):
    CHECK = 'W'
    FILL = 'B'
    if r > 0 and c > 0 and r >= len(board) and c >= len(board[0]):
        if VISITED_MAP[r][c] == 1:
            return True
        else:
            VISITED_MAP[r][c] = 1
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
        return True
    elif board[r][c] == FILL:
        return False
    else:
        p1 = dfs(board, r + 1, c, VISITED_MAP)
        if p1:
            VISITED_MAP[r][c] = 1
        p2 = dfs(board, r - 1, c, VISITED_MAP)
        if p2:
            VISITED_MAP[r][c] = 1
        p3 = dfs(board, r, c + 1, VISITED_MAP)
        if p3:
            VISITED_MAP[r][c] = 1
        p4 = dfs(board, r, c - 1, VISITED_MAP)
        if p4:
            VISITED_MAP[r][c] = 1

        if (p1 or p2 or p3 or p4):
            board[r][c] = CHECK
        else:
            board[r][c] = FILL



def print_board(maze):
    print("-----BOARD-----")
    for r in range(len(maze)):
        print(maze[r])
    print()

data = [['W','B','B'],
        ['B','W','B'],
        ['W','B','W']]
test = fill_surrounded_regions(data)


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(generic_test.generic_test_main("matrix_enclosed_regions.py",'matrix_enclosed_regions.tsv',fill_surrounded_regions_wrapper))
