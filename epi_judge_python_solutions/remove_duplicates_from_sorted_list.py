from test_framework import generic_test


def remove_duplicates(L):
    original = L
    unique_vals = set()
    while(L != None):
        key = L.data
        if key in unique_vals:
            if L.next == None:
                L.data = None
            else:
                L.data = L.next.data
                L.next = L.next.next
        else:
            unique_vals.add(key)
            L = L.next
    return original



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
