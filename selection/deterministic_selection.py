def chunks(array, n):
    out = []
    for i in range(0, len(array), n):
        out.append(array[i:i + n])
    return out

def median(array):
    if len(array) % 2 == 0:
        return array[int((len(array)/2)-1)]
    return array[int(((len(array) - 1) / 2))]

def deterministic_selection(array, length, i):
    if length == 1:
        return array[0]

    groups = chunks(array, 5)
    sorted_groups = [merge_sort(i) for i in groups]
    C = [median(i) for i in sorted_groups]
    p = deterministic_selection(C, len(C), int(round((len(C)/2),0)))

    p = array.index(p)

    new_start, new_p = array[p], array[0]
    array[p], array[0] = new_p, new_start
    array, p = partition(array, 0, length - 1)

    left = array[0: p]
    right = array[p + 1: length]

    j = p

    if j == i:
        return array[p]
    elif j > i:
        return deterministic_selection(left, len(left), i)
    else:
        return deterministic_selection(right, len(right), i-j)
