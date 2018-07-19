from test_framework import generic_test


def find_nearest_repetition(paragraph):
    hashmap = dict()
    word_list = list(paragraph)
    shortest_distance = float('inf')
    for i in range(len(word_list)):
        key = word_list[i]
        if key in hashmap:
            temp_distance = abs(hashmap[key] - i)
            if temp_distance < shortest_distance:
                shortest_distance = temp_distance
        hashmap[key] = i
    if shortest_distance == float('inf'):
        return -1
    else:
        return shortest_distance




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
