from test_framework import generic_test


def minimum_messiness(words, line_length):
    remaining_blanks = line_length - len(words[0])
    min_mess = ([remaining_blanks**2] + [float('inf')] * (len(words) - 1))
    for i in range(1, len(words)):
        remaining_blanks = line_length - len(words[i])
        min_mess[i] = min_mess[i - 1] + remaining_blanks**2
        for j in reversed(range(i)):
            remaining_blanks -= len(words[j]) + 1
            if remaining_blanks < 0:
                break
            first_j_messiness = 0 if j - 1 < 0 else min_mess[j - 1]
            current_line_messiness = remaining_blanks**2
            min_mess[i] = min(min_mess[i],
                                   first_j_messiness + current_line_messiness)
    return min_mess[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))
