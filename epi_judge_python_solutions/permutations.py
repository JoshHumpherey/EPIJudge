from test_framework import generic_test, test_utils
import itertools

def pythonic_permutations(A):
    answer = list(itertools.permutations(A))
    return answer

def permutations(A):
    results = []
    def build_perms(i):
        if i == len(A)-1:
            results.append(A)
            return
        else:
            for j in range(i, len(A)):
                A[i],A[j] = A[j],A[i]
                build_perms(i+1)
                A[i],A[j] = A[j],A[i]
    build_perms(0)
    return results



if __name__ == '__main__':
    exit(generic_test.generic_test_main("permutations.py", 'permutations.tsv',permutations,test_utils.unordered_compare))
