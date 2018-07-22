import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, start, end):
    print_maze(maze)
    print([end.row, end.col])
    r = start.row
    c = start.col
    is_path = dfs(maze, r, c, end)
    print(is_path)
    return is_path

def dfs(maze, r, c, target):
    if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]) or maze[r][c] != 0:
        return False
    elif r == target.row and c == target.col:
        return True
    else:
        maze[r][c] = 1
        p1 = dfs(maze, r+1, c, target)
        p2 = dfs(maze, r-1, c, target)
        p3 = dfs(maze, r, c+1, target)
        p4 = dfs(maze, r, c-1, target)
        return (p1 or p2 or p3 or p4)


def print_maze(maze):
    print("-----MAZE-----")
    for r in range(len(maze)):
        print(maze[r])
    print()


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
