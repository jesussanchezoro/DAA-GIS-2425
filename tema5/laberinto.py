import copy

def init_lab():
    f = 10
    c = 10
    lab = []
    for _ in range(f):
        lab.append([0] * c)
    walls = [(0,2),(0,7),
             (1,0),(1,2),(1,5),(1,6),(1,8),
             (2,6),(2,8),
             (3,1),(3,4),(3,5),(3,6),
             (4,2),(4,3),(4,7),
             (5,5),(5,7),
             (6,0),(6,3),(6,4),(6,7),(6,9),
             (7,1),(7,2),(7,8),(7,9),
             (8,0),(8,5),(8,7),(8,8),
             (9,2),(9,4),(9,5)]
    for f,c in walls:
        lab[f][c] = float("Inf")
    return lab


def init_sol(lab):
    sol = copy.deepcopy(lab)
    sol[len(sol)-1][len(sol[0])-1] = float("Inf")
    return sol


def is_sol(lab, f, c):
    return f == len(lab)-1 and c == len(lab[0])-1

def is_better(lab, best):
    n = len(lab)-1
    m = len(lab[0]) - 1
    return lab[n][m] < best[n][m]


def is_feasible(lab, f, c):
    return (0 <= f < len(lab) and 0 <= c < len(lab[0])) and lab[f][c] == 0


def print_lab(lab):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == float("Inf"):
                print("*", end=" ")
            else:
                print(lab[i][j], end=" ")
        print()

def lab_va(lab, best, f, c, k):
    if is_sol(lab, f, c):
        if is_better(lab, best):
            best = copy.deepcopy(lab)
    else:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        for d in dir:
            new_f = f + d[0]
            new_c = c + d[1]
            if is_feasible(lab, new_f, new_c):
                lab[new_f][new_c] = k
                best = lab_va(lab, best, new_f, new_c, k+1)
                lab[new_f][new_c] = 0
    return best


lab = init_lab()
best = init_sol(lab)
ini = (0,0)
k = 1
lab[ini[0]][ini[1]] = k
best = lab_va(lab, best, ini[0], ini[1], k+1)
print_lab(best)