from test_framework import generic_test
import collections

def num_combinations_for_final_score(target, map):
    results = []
    def build_path(target, map, current):
        if sum(current) == target:
            results.append(current)
            return
        elif sum(current) > target:
            return
        else:
            for play in map:
                build_path(target, map, current + [play])
            return

    for val in map:
        build_path(target, map, [val])
    return results




#TEST = num_combinations_for_final_score(8, [2,3,7])
#print(TEST)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
