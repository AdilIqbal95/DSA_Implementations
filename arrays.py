#  Quick sort


# Merge Sort

def merge_sort(array):
    array_length = len(array)
    middle_index = array_length // 2
    if array_length <= 1:
        return array

    array_one = array[:middle_index]
    array_two = array[middle_index:]

    sorted_array_one = merge_sort(array_one)

    sorted_array_two = merge_sort(array_two)

    return merge_arrays(sorted_array_one, sorted_array_two)

def merge_arrays(array1, array2):
    merged_arr = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] > array2[j]:
            merged_arr.append(array2[j])
            # print(f'if {merged_arr}')
            j += 1
        else:
            merged_arr.append(array1[i])
            # print(f'else {merged_arr}')
            i += 1

    merged_arr.extend(array1[i:])
    # print(f'arr1 {merged_arr}')
    merged_arr.extend(array2[j:])
    # print(f'arr2 {merged_arr}')

    return merged_arr

def merge_sort_test():
    # mergeArrays test cases
    a = [2, 8, 15, 18]
    b = [5, 9, 12, 17]
    # mergeSort test cases
    c = [2, 5, 7, 3, 10, 4, 1, 9]  # even length
    d = [2, 6, 5, 1, 7, 4, 3]  # odd length

    print(merge_sort(d))

# merge_sort_test()

# Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

def bs_test():
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    target1 = 6

    arr2 = [2, 5, 7, 9, 12, 15, 18, 21, 25, 28, 31, 34, 38, 41, 45, 49, 53, 57, 62, 67]
    target2 = 13

    print(binary_search(arr2,target2))

# bs_test()


# Two Pointers



# Sliding Window
# E.g. 1 - Fixed length window
'''
Find max sum subarray of a fixed size K

Example input:
[4, 2, 1, 7, 8, 1, 2, 8, 1, 0]

'''

def find_max_sum_subarray(arr, k):
    max_value = float('-inf')
    current_running_sum = 0

    for i in range(len(arr)):
        current_running_sum += arr[i]

        if i >= k - 1:
            max_value = max(max_value, current_running_sum)
            current_running_sum -= arr[i - (k - 1)]

    return max_value

def sliding_window_test_eg1():
    arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    k = 3
    print(find_max_sum_subarray(arr, k))

# sliding_window_test_eg1()

# E.g. 2 - Dynamic window
'''
Find smallest subarray with sum >= 8

Example input:
[4, 2, 2, 7, 8, 1, 2, 8, 10]

'''

def smallest_subarray(arr, target_sum):
    min_window_size = float('inf')
    current_window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        current_window_sum += arr[window_end]

        while current_window_sum >= target_sum:
            min_window_size = min(min_window_size, window_end - window_start + 1)
            current_window_sum -= arr[window_start]
            window_start += 1

    return min_window_size #if min_window_size != float('inf') else 0 <- this part adde by chatgpt, possibly to handle edgecases?

def sliding_window_test_eg2():
    arr = [4, 2, 2, 7, 8, 1, 2, 8, 10]
    targetSum = 8
    print(smallest_subarray(arr, targetSum))

# sliding_window_test_eg2()

# E.g. 3 - Dynamic variant w/ auxillary DS
'''
Find longest substring length with k distinct characters

Example input:
['A','A','A','H','H','I','B','C']
'''
#  TODO

