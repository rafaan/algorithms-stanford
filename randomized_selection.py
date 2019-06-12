def randomized_selection(array, length, i):
    if length == 1:
        return array[0]

    p = np.random.randint(0, len(array))
    new_start, new_p = array[p], array[0]
    array[p], array[0] = new_p, new_start
    array, p = partition(array, 0, length - 1)

    left = array[0: p]
    right = array[p + 1: length]

    j = p

    if j == i:
        return array[p]
    elif j > i:
        return randomized_selection(left, len(left), i)
    else:
        return randomized_selection(right, len(right), i-j)
