def init_graph():
    data = {}
    data['n'] = 4
    data['g'] = [[1,2,3], [0], [0,3], [0,2]]
    return data


def init_sol(g):
    sol = [0] * g['n']
    return sol


def is_sol(g, node):
    return node == g['n']


def is_feasible(g, sol, node, color):
    adj_list = g['g'][node]
    for adj in adj_list:
        if adj < node and sol[adj] == color:
            return False
    return True


def coloring_va(g, m, sol, node):
    if is_sol(g, node):
        found = True
    else:
        found = False
        color = 1
        while not found and color <= m:
            if is_feasible(g, sol, node, color):
                sol[node] = color
                sol, found = coloring_va(g, m, sol, node+1)
                if not found:
                    sol[node] = 0
            color += 1
    return sol, found


g = init_graph()
m = 3
node = 0
sol = init_sol(g)
sol, is_sol = coloring_va(g, m, sol, node)
if is_sol:
    print(sol)
else:
    print('No solution found')