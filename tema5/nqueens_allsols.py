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


def nqueens(sol, n, row):
    if is_sol(sol, row):
        print(sol)
    else:
        col = 0
        while col < n:
            if is_feasible(sol, row, col):
                sol[row] = col
                nqueens(sol, n, row+1)
                sol[row] = -1
            col += 1


n = 12
sol = [-1] * n
ini = time.time()
nqueens(sol, n, 0)
print("TOTAL: "+str(time.time()-ini))
