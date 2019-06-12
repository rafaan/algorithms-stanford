def merge(left, right):
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr += left[i:]
    arr += right[j:]

    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge_and_count_split_inversions(left, right):
    i = 0
    j = 0
    arr = []
    inv = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
            inv += len(left) - i

    arr += left[i:]
    arr += right[j:]

    return arr, inv

def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr)//2

    left, l_inv = merge_sort_and_count(arr[:mid])
    right, r_inv = merge_sort_and_count(arr[mid:])
    result, split_inv = merge_and_count_split_inversions(left, right)
    return result, l_inv + r_inv + split_inv
