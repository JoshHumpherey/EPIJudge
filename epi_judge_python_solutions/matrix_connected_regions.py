import collections
import time
from test_framework import generic_test

def flip_color(r, c, image):
    print_maze(image)
    TARGET_COLOR = image[r][c]
    if TARGET_COLOR == 1:
        FILL = 0
    else:
        FILL = 1
    queue = [[r,c]]
    while queue:
        pair = queue.pop()
        r,c = pair[0], pair[1]
        if r >= 0 and c >= 0 and r < len(image) and c < len(image) and image[r][c] == TARGET_COLOR:
            image[r][c] = FILL
            #print_maze(image)
            #time.sleep(1)
            if r + 1 < len(image):
                queue.append([r+1,c])
            if r -1 >= 0:
                queue.append([r-1,c])
            if c + 1 < len(image[0]):
                queue.append([r,c+1])
            if c - 1 >= 0:
                queue.append([r,c-1])
    return image



def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image

def print_maze(maze):
    print("-----MAZE-----")
    for r in range(len(maze)):
        print(maze[r])
    print()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
