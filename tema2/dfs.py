## Definicion del algoritmo
def dfs(g):
    n = len(g)-1
    visited = set()
    # visited = [False] * n
    for v in range(1, n):
        if v not in visited:
        # if not visited[v]:
            dfs_rec(g, v, visited)

def dfs_rec(g, v, visited):
    visited.add(v)
    print(v, end=" ")
    for adj in g[v]:
        if adj not in visited:
            dfs_rec(g, adj, visited)

## Datos
g = [
    [],
    [2, 4, 8],
    [1, 3, 4],
    [2, 4, 5],
    [1, 2, 3, 7],
    [3, 6],
    [5, 7],
    [4, 6, 9],
    [1, 9],
    [7, 8]
]

## Llamada a la funcion
dfs(g)