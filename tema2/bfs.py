from collections import deque

def bfs(g):
    n = len(g)-1
    visited = [False] * (n+1)
    for v in range(1, n):
        if not visited[v]:
            bfs_aux(g, v, visited)

def bfs_aux(g, v, visited):
    q = deque()
    visited[v] = True
    print(v, end=" ")
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                print(adj, end=" ")
                visited[adj] = True
                q.append(adj)



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

bfs(g)