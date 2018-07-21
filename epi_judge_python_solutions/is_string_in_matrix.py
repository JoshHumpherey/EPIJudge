from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    print_grid(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == S[0]:
                #print("DFS on: " + str([r,c]))
                result = dfs(grid, 0, r, c, S)
                #print("Result: " + str(result))
                if result == True:
                    return True
    return False

def dfs(grid, index, r, c, S):
    #print("Checking " + str([r,c]) + " with a value of: " + str(grid[r][c]) + " ---- Expecting: " + str(S[index]))
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return False
    elif S[index] == grid[r][c] and len(S) -1 == index:
        return True
    elif S[index] == grid[r][c]:
        #print("For " + str(S[index]) + " we found TRUE")
        res1 = dfs(grid, index + 1, r+1, c, S)
        res2 = dfs(grid, index + 1, r-1, c, S)
        res3 = dfs(grid, index + 1, r, c+1, S)
        res4 = dfs(grid, index + 1, r, c-1, S)
        return (res1 or res2 or res3 or res4)
    else:
        return False

def print_grid(grid):
    print("Grid: " )
    for r in range(len(grid)):
        print(grid[r])
    print()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
