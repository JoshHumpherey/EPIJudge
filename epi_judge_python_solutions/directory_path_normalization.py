from test_framework import generic_test


def shortest_equivalent_path(path):
    file_list = path.split('/')
    print(file_list)
    if len(file_list) <= 3:
        return path

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
