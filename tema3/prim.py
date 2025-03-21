import random


def select_min(candidates, visited):
    node = None
    weight = float("Inf")
    for i in range(1, len(candidates)):
        if not visited[i] and candidates[i] < weight:
            node = i
            weight = candidates[i]
    return node, weight


def prim(g):
    n = len(g)
    initial = random.randint(1, n-1)
    sol = 0
    visited = [False] * n
    candidates = [float("Inf")] * n
    for start, end, weight in g[initial]:
        candidates[end] = weight
    visited[initial] = True
    for _ in range(2, n):
        next_node, cost = select_min(candidates, visited)
        if cost < float("Inf"):
            visited[next_node] = True
            sol += cost
        for start, end, weight in g[next_node]:
            if not visited[end]:
                candidates[end] = min(candidates[end], weight)
    return sol







g = [
    [],
    [(1,3,1), (1,4,2), (1,7,6)],
    [(2,5,2), (2,6,4), (2,7,7)],
    [(3,1,1), (3,4,3), (3,7,5)],
    [(4,1,2), (4,3,3), (4,5,1), (4,6,9)],
    [(5,2,2), (5,4,1), (5,7,8)],
    [(6,2,4), (6,4,9)],
    [(7,1,6), (7,2,7), (7,3,5), (7,5,8)]
]

sol = prim(g)
print(sol)