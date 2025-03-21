
def select_min(distances, visited):
    min_dist = float('inf')
    next_node = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            next_node = i
    return next_node


def dijkstra(g, start):
    n = len(g)-1
    distances = [float('inf') for _ in range(n+1)] # SOL
    visited = [False for _ in range(n + 1)]
    distances[start] = 0
    visited[start] = True
    for u, v, w in g[start]:
        distances[v] = w
    for _ in range(2, n+1):
        next_node = select_min(distances, visited)
        visited[next_node] = True
        for u, v, w in g[next_node]:
            distances[v] = min(distances[v], distances[u]+w)
    return distances

g = [
    [],
    [(1,2,5), (1,4,3)],
    [(2,5,1)],
    [],
    [(4,2,1),(4,3,11),(4,5,6)],
    [(5,3,1)]
]

start = 1
sol = dijkstra(g, start)
print(sol)