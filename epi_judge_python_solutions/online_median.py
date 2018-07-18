import heapq

from test_framework import generic_test


def online_median(arr):
    min_heap = [] # stores greater/right half of the array
    max_heap = [] # stores less/left half of the array
    results = []
    for num in arr:
        if len(min_heap) == 0:
            heapq.heappush(min_heap, num)
        elif len(max_heap) == 0:
            conv_num = (-1)*num
            heapq.heappush(max_heap, conv_num)
        else:
            left_num = max_heap[0]*(-1)
            right_num = min_heap[0]
            if left_num > num:
                conv_num = num*(-1)
                heapq.heappush(max_heap, conv_num)
            else:
                heapq.heappush(min_heap, num)
        max_heap, min_heap = balance_heaps(max_heap, min_heap)
        temp = calculate_median(max_heap, min_heap)
        results.append(temp)
    return results

def balance_heaps(max_heap, min_heap):
    if len(max_heap) > 0 and len(min_heap) > 0:
        if (len(max_heap) > len(min_heap)):
            temp = heapq.heappop(max_heap)
            temp *= (-1)
            heapq.heappush(min_heap, temp)
            if (max_heap[0]*(-1) > min_heap[0]):
                left_val = heapq.heappop(max_heap)*(-1)
                right_val = heapq.heappop(min_heap)
                heapq.heappush(min_heap, left_val)
                heapq.heappush(max_heap, right_val)

        elif len(min_heap) > len(max_heap):
            temp = heapq.heappop(min_heap)
            temp *= (-1)
            heapq.heappush(max_heap, temp)
            if (max_heap[0]*(-1) > min_heap[0]):
                left_val = heapq.heappop(max_heap)*(-1)
                right_val = heapq.heappop(min_heap)
                heapq.heappush(min_heap, left_val)
                heapq.heappush(max_heap, right_val)
    return max_heap, min_heap

def calculate_median(max_heap, min_heap):
    #print("MAX: " + str(max_heap) + " MIN: " + str(min_heap))
    if len(max_heap) > len(min_heap):
        switch_num = max_heap[0]
        num = (-1)*switch_num
        return num
    elif len(max_heap) < len(min_heap):
        num = min_heap[0]
        return num
    else:
        num1 = min_heap[0]
        switch_num = max_heap[0]
        num2 = (-1)*switch_num
        return float((num1 + num2)/2)


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
