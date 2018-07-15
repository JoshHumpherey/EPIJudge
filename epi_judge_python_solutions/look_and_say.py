import itertools

from test_framework import generic_test


def look_and_say(n):
    print()
    pattern = dict()
    pattern[1] = "1"
    pattern[2] = "11"
    pattern[3] = "21"
    pattern[4] = "1211"
    for i in range(5, n+1):
        temp = []
        to_parse = pattern[i-1]
        current_char = to_parse[0]
        current_count = 1
        for j in range(1, len(to_parse)):
            if to_parse[j] == current_char:
                if len(to_parse)-1 == j:
                    partial = str(current_count+1) + str(current_char)
                    temp.append(partial)
                else:
                    current_count += 1
                    current_char = to_parse[j]
            else:
                partial = str(current_count) + str(current_char)
                temp.append(partial)
                current_count = 1
                current_char = to_parse[j]
                if len(to_parse)-1 == j:
                    partial = str(current_count) + str(current_char)
                    temp.append(partial)
        final_string = ''.join(temp)
        pattern[i] = final_string
    for i in range(1, n):
        print(str(i) + ": " + str(pattern[i]))

    return pattern[n]

result = look_and_say(2)
print(result)


# Pythonic solution uses the power of itertools.groupby().
def look_and_say_pythonic(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
