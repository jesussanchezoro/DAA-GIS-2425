from collections import deque

def bfs(g):
    n = len(g)
    visited = [False] * n
    ncc = 0
    for v in range(n):
        if not visited[v]:
            ncc += 1
            bfs_aux(g, v, visited)
    return ncc

def bfs_aux(g, v, visited):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True





n, m = map(int, input().strip().split())
g = []
for _ in range(n):
    g.append([])
for _ in range(m):
    u, v = map(int, input().strip().split())
    g[u].append(v)
    g[v].append(u)

ncc = bfs(g)
print(ncc)