import random
import numpy as np

def partition(array, l, r):
    p = array[l]
    i = l + 1

    for j in range(l+1, r+1):
        if array[j] < p:
            new_i, new_j = array[j], array[i]
            array[i], array[j] = new_i, new_j
            i += 1

    new_l, new_i_minus_one = array[i-1], array[l]
    array[l], array[i-1] = new_l, new_i_minus_one
    return array, i-1

# Choose P functions
def randomized_p(array):
    return np.random.randint(0, len(array))

def first_element(array):
    return 0

def final_element(array):
    return len(array) - 1

def median_of_three(array):
    if len(array) % 2 == 0:
        mid = array[int((len(array)/2)-1)]
    else:
        mid = array[int(((len(array) - 1) / 2))]

    first = array[0]
    last = array[-1]

    sorted_array = quicksort([first, mid, last], 3, first_element)
    return array.index(sorted_array[1])

def quicksort(array, length, p_func):
    if length <= 1:
        return array

    quicksort.count += (len(array) - 1)

    p = p_func(array)
    new_start, new_p = array[p], array[0]
    array[p], array[0] = new_p, new_start
    array, p = partition(array, 0, length - 1)

    left = array[0: p]
    right = array[p + 1: length]

    left_count = len(left) - 1
    right_count = len(right) - 1

    left_array = quicksort(left, len(left), p_func)
    mid_array = [array[p]]
    right_array = quicksort(right, len(right), p_func)

    return left_array + mid_array + right_array

quicksort.count = 0
quicksort([5,4,6,2,1], 5, first_element)
quicksort.count
