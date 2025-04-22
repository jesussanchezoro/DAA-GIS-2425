

def merge(left, right, v):
    l = 0
    r = 0
    i = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            v[i] = left[l]
            l += 1
        else:
            v[i] = right[r]
            r += 1
        i += 1

    if r == len(right):
        f = l
        resto = left
    else:
        f = r
        resto = right

    for j in range(f, len(resto)):
        v[i] = resto[j]
        i += 1


def merge_sort(v):
    if len(v) == 1:
        return
    else:
        mid = len(v) // 2
        left = v[:mid]
        right = v[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, v)


v = [3, 1, 4, 1, 7, 9, 2, 6, 5, 3, 5, 8]
merge_sort(v)
print(v)