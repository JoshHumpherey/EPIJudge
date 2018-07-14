import functools

from test_framework import generic_test
import math

MAPPING = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
           'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
MULTIPLIER = 26

def ss_decode_col_id(col):
    if len(col) == 1:
        return MAPPING[col]
    col_list = list(col)
    running_total = 0
    power = len(col_list)-1
    for i in range(len(col_list)-1):
        key = col_list[i]
        running_total += ((MULTIPLIER**power)*MAPPING[key])
        power -= 1

    key = col_list[-1]
    running_total += MAPPING[key]
    return running_total





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
