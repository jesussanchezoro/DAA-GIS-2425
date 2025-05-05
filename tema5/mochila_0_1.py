import copy

def init_data():
    data = {}
    data['n'] = 4
    data['W'] = 8
    data['w'] = [2,3,4,5]
    data['v'] = [3,5,6,10]
    return data

def init_sol(data):
    sol = {}
    sol['obj'] = [0] * data['n']
    sol['w'] = 0
    sol['v'] = 0
    return sol


def add(sol, data, i):
    sol['obj'][i] = 1
    sol['w'] += data['w'][i]
    sol['v'] += data['v'][i]


def remove(sol, data, i):
    sol['obj'][i] = 0
    sol['w'] -= data['w'][i]
    sol['v'] -= data['v'][i]


def best(sol_1, sol_2):
    if sol_1['v'] > sol_2['v']:
        best_sol = copy.deepcopy(sol_1)
    else:
        best_sol = copy.deepcopy(sol_2)
    return best_sol


def is_solution(sol, data):
    return sol['w'] + min(data['w']) > data['W']


def is_feasible(sol, data, i):
    return sol['w'] + data['w'][i] <= data['W']

def knapsack_0_1(data, sol, best_sol, k):
    if is_solution(sol, data):
        best_sol = best(best_sol, sol)
    else:
        for i in range(k, data['n']):
            if is_feasible(sol, data, i):
                add(sol, data, i)
                best_sol = knapsack_0_1(data, sol, best_sol, i+1)
                remove(sol, data, i)
    return best_sol



data = init_data()
sol = init_sol(data)
best_sol = init_sol(data)
best_sol = knapsack_0_1(data, sol, best_sol, 0)
print(best_sol)