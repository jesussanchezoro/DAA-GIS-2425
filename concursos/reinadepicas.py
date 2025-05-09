
def is_sol(f, c, end, rewards):
    return f == end[0] and c == end[1] and rewards == 0


def is_feasible(lab, new_f, new_c):
    return (0 <= new_f < len(lab) and 0 <= new_c < len(lab[0]) and -1 <=+
    lab[new_f][new_c] <= 0)


def lab_bt(lab, best, f, c, k, rewards, end):
    if is_sol(f, c, end, rewards):
        best = min(best, k-1)
    else:
        desp = [[1,0], [0,1], [-1,0], [0,-1]]
        for d in desp:
            new_f = f + d[0]
            new_c = c + d[1]
            if is_feasible(lab, new_f, new_c):
                old_val = lab[new_f][new_c]
                if old_val == -1:
                    rewards -= 1
                lab[new_f][new_c] = k
                best = lab_bt(lab, best, new_f, new_c, k+1, rewards, end)
                lab[new_f][new_c] = old_val
                if old_val == -1:
                    rewards += 1
    return best



def fill_turret(lab, n, m, x, y):
    minus_rewards = 0
    for i in range(max(0,x-1), min(n,x+2)):
        for j in range(max(0,y-1), min(m,y+2)):
            if lab[i][j] == -1:
                minus_rewards += 1
            lab[i][j] = -2
    return minus_rewards


n, m = map(int, input().strip().split())
lab = []
start = None
end = None
rewards = 0
for _ in range(n):
    lab.append([0] * m)
for i in range(n):
    line = input().strip().split()
    for j in range(m):
        if line[j] == 'w':
            lab[i][j] = -2
        elif line[j] == 't':
            rewards -= fill_turret(lab, n, m, i, j)
        elif line[j] == 'r' and lab[i][j] >= 0:
            rewards += 1
            lab[i][j] = -1
        elif line[j] == 's':
            start = (i,j)
        elif line[j] == 'e':
            end = (i,j)

lab[start[0]][start[1]] = 1
best = lab_bt(lab, float("Inf"), start[0], start[1], 2, rewards, end)
print(best)