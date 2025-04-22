
def binary_search(v, number, low, high):
    if low > high:
        return -low
    mid = (low + high) // 2
    if v[mid] == number:
        return mid
    if number < v[mid]:
        return binary_search(v, number, low, mid - 1)
    else:
        return binary_search(v, number, mid + 1, high)


v = [1, 3, 3, 5, 6, 7, 9]

number = 4
index = binary_search(v, number, 0, len(v)-1)
if index >= 0:
    print(index)
else:
    print("No encontrado, estaria despues de "+str(v[-index-1]))