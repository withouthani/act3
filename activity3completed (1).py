#Phase 1: Data Generation and Initial Sorting (Insertion Sort)

import random
import time

"""def generate_sorted_data(size):
    
    size = [random.randint(1, 100) for _ in range(size)]
    
    for i in range(1, len(size)):
        j = i
        while j > 0 and size[j - 1] > size[j]:
            size[j - 1], size[j] = size[j], size[j - 1]
            j -= 1
    
    print(size)
generate_sorted_data(6)"""

#phase 2

"""def binary_search(array_a,start, end, target_value):
    midpoint= (start+end)//2
    print("printing the midpoint: ", midpoint)

    #base case
    if start>end:
        return-1
    if array_a[midpoint] < target_value:
        return binary_search(array_a, midpoint+1, end, target_value) 
    elif array_a[midpoint] > target_value:
        return binary_search(array_a, start, midpoint-1, target_value)
    elif array_a[midpoint] == target_value:
        return midpoint


def main():
    array_a = [5, 7, 8, 12, 23, 29, 32, 34, 40, 62]
    target_value= int(input("enter the value you want to search: "))

    result = binary_search(array_a,0, len(array_a)-1, target_value) 
    if result ==-1:
        print("target value not found")
    else:
        print("target value found at index", array_a.index(target_value))

if __name__ == "__main__":
    main()
"""

#phase 3

"""


def array_split(arr):
    if arr is None or len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        # Split and recursively sort each half
        left_half = array_split(arr[:mid])
        right_half = array_split(arr[mid:])
        # Merge the sorted halves
        return merge(left_half, right_half)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    # Merge sorted lists
    if left[0] <= right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

def main():
    begin = time.perf_counter()

    arr1 = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] 
    sorted_arr_1 = array_split(arr1)  # Use the returned sorted array

    arr2 = [random.randint(1, 100) for _ in range(990)]
    sorted_arr_2 = array_split(arr2)  # Use the returned sorted array


    arr3 = sorted_arr_1 + sorted_arr_2

    print("Original array:", arr1)

    print("Sorted array:", arr3)
    
    end = time.perf_counter()
    total = end - begin
    print("Total time taken is:", total)

if __name__ == "__main__":
    main()
"""

#phase 4


import time

# will make a sorted list of the given size
def make_sorted_list(size):
    return list(range(size))  # will generate a sorted list from 0 to size -1

# It performs a binary search finding the index of a target value
def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == value:
            return middle
        elif arr[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return None

# It performs a linear search to find the index of a target value in a list
def linear_search(arr, value):
    for idx in range(len(arr)):
        if arr[idx] == value:
            return idx
    return None


sorted_list = make_sorted_list(1000)

# timing binary search
binary_search_start = time.perf_counter()
binary_search(sorted_list, 72)
binary_search_end = time.perf_counter()

# timing linear search
linear_search_start = time.perf_counter()
linear_search(sorted_list, 72)
linear_search_end = time.perf_counter()

# calculting the time of the searches
binary_search_duration = binary_search_end - binary_search_start
linear_search_duration = linear_search_end - linear_search_start

# printing the result
print('Search time for Binary Search is :', binary_search_duration)
print('Search time for Linear Search is :', linear_search_duration)