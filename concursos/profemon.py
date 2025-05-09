
def binary_search(profemon, start, end, search):
    if start > end:
        return start
    else:
        mid = (start + end) // 2
        if search == profemon[mid]:
            return mid
        else:
            if search > profemon[mid]:
                return binary_search(profemon, mid+1, end, search)
            else:
                return binary_search(profemon, start, mid-1, search)



n, students = map(int, input().strip().split())
profemon = sorted(list(map(int, input().strip().split())))
max_profemon = 0
best_student = []
for _ in range(students):
    stu_id, p1, p2 = map(int, input().strip().split())
    p1_idx = binary_search(profemon, 0, n-1, p1)
    p2_idx = binary_search(profemon, 0, n-1, p2)
    if max_profemon < p2_idx-p1_idx+1:
        max_profemon = p2_idx-p1_idx+1
        best_student = []
        best_student.append(stu_id)
    elif max_profemon == p2_idx-p1_idx+1:
        best_student.append(stu_id)
for s in best_student:
    print(str(s), end=" ")
print()
print(str(max_profemon))