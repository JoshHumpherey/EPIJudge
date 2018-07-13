import collections

from test_framework import generic_test

def flip_color(r, c, image):
    target_color = image[r][c]
    result = dfs(r, c, image, target_color)
    return result

def dfs(r, c, image, target):
    if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != target:
        return image
    else:
        image[r][c] = True
        img1 = dfs(r+1, c, image, target)
        img2 = dfs(r-1, c, img1, target)
        img3 = dfs(r, c+1, img2, target)
        img4 = dfs(r, c-1, img3, target)
        return img4


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
