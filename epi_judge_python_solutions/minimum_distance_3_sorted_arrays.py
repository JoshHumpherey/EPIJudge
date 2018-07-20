from test_framework import generic_test


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    target_len = len(sorted_arrays)
    master_array = []
    mapping = dict()
    min_val = float('inf')
    max_val = float('-inf')
    index = 0
    for array in sorted_arrays:
        for key in array:
            if key > max_val:
                max_val = key
            if key < min_val:
                min_val = key
            mapping[key] = index
            master_array.append(key)
        index += 1
    sorted_master = sorted(master_array)
    pairs = []
    for i in range(len(sorted_master)):
        temp_pair = []
        temp_set = set()
        for j in range(i, len(sorted_master)):
            key = sorted_master[j]
            val = mapping[key]
            if val not in temp_set:
                temp_set.add(val)
                temp_pair.append(key)
            if len(temp_pair) == target_len:
                pairs.append(temp_pair)
                break

    lowest_diff = float('inf')
    lowest_pair = None
    pair_diff = lambda diff: (abs(max(pair) - min(pair)))
    for pair in pairs:
        res = pair_diff(pair)
        print("Pair Diff: " + str(res))
        if res < lowest_diff:
            lowest_diff = res
            lowest_pair = pair
    return lowest_diff






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
