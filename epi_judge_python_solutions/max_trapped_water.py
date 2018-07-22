from test_framework import generic_test


def get_max_trapped_water(heights):
    max_area = 0
    for i in range(len(heights)):
        temp = find_max_for_index(i, heights[i], heights)
        if temp > max_area:
            max_area = temp
    reversed_heights = heights[::-1]
    for i in range(len(reversed_heights)):
        temp = find_max_for_index(i, reversed_heights[i], reversed_heights)
        if temp > max_area:
            max_area = temp
    return max_area



def find_max_for_index(index, target_height, heights):
    area = lambda l,h : l * h
    if index >= len(heights):
        return 0
    local_max = 0
    for i in range(index+1, len(heights)):
        if heights[i] >= target_height:
            res = area(target_height, (i - index))
            if res > local_max:
                local_max = res
    return local_max






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py", "max_trapped_water.tsv", get_max_trapped_water))
