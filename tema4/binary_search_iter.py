
def binary_search(v, number):
    low = 0
    high = len(v) - 1
    while low <= high:
        mid = (low + high) // 2
        if number == v[mid]:
            return mid
        if number < v[mid]:
            high = mid-1
        else:
            low = mid+1
    return -low


v = [1, 3, 3, 5, 6, 7, 9]

number = 6
index = binary_search(v, number)
if index >= 0:
    print(index)
else:
    print("No encontrado, estaria despues de "+str(v[-index-1]))