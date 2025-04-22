
def pivot(v, left, right):
    pivote = v[left]
    i = left + 1
    while i < right and v[i] < pivote:
        i += 1
    j = right
    while j > left and v[j] > pivote:
        j -= 1
    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        while v[i] < pivote:
            i += 1
        j -= 1
        while v[j] > pivote and j > left:
            j -= 1
    v[left], v[j] = v[j], v[left]
    return j

def quicksort(v, i, j):
    if i > j:
        return v
    else:
        pivote = pivot(v, i, j)
        quicksort(v, i, pivote - 1)
        quicksort(v, pivote + 1, j)


v = [4, 6, 4, 67, 4, 3, 4, 4, 65, 34, 5, 3, 5, 3]
quicksort(v, 0, len(v)-1)
print(v)