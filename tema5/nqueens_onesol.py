import time


def is_sol(sol, row):
    return row == len(sol)


def is_feasible(sol, row, col):
    is_feas = True
    i = 1
    while is_feas and i <= row:
        feas_col = sol[row-i] == -1 or sol[row-i] != col
        feas_diag1 = sol[row-i] == -1 or col-i < 0 or sol[row-i] != col - i
        feas_diag2 = sol[row-i] == -1 or col+1 >= len(sol) or sol[row-i] != col + i
        is_feas = feas_col and feas_diag1 and feas_diag2
        i += 1
    return is_feas


def nqueens(sol, n, found, row):
    if is_sol(sol, row):
        found = True
    else:
        col = 0
        while not found and col < n:
            if is_feasible(sol, row, col):
                sol[row] = col
                sol, found = nqueens(sol, n, found, row+1)
                if not found:
                    sol[row] = -1
            col += 1
    return sol, found


n = 20
sol = [-1] * n
ini = time.time()
sol, found = nqueens(sol, n, False, 0)
if found:
    print(sol)
else:
    print("No solution found")
print("TOTAL: "+str(time.time()-ini))
