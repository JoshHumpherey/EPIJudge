from test_framework import generic_test


def calculate_largest_rectangle(heights):
    if len(heights) == 0:
        return 0

    area = lambda l,w : l*w
    max_height = max(heights)
    max_area = 0
    for h in range(1, max_height + 1):
        longest_sequence = 0
        biggest_area = 0
        for i in range(len(heights)):
            if h <= heights[i]:
                longest_sequence += 1
                if i == len(heights) - 1:
                    my_area = area(longest_sequence, h)
                    if my_area > biggest_area:
                        biggest_area = my_area
            else:
                my_area = area(longest_sequence, h)
                if my_area > biggest_area:
                    biggest_area = my_area
                longest_sequence = 0
        if biggest_area > max_area:
            max_area = biggest_area
    return max_area



if __name__ == '__main__':
    exit(generic_test.generic_test_main("largest_rectangle_under_skyline.py",'largest_rectangle_under_skyline.tsv',calculate_largest_rectangle))
