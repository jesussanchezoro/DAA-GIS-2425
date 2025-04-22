from queue import PriorityQueue

def dijkstra(g):
    n = len(g)
    dist = [float("inf")] * n
    pq = PriorityQueue()
    dist[0] = 0
    pq.put((0,0))
    while not pq.empty():
        du, u = pq.get()
        for v, dv in g[u]:
            alt = dist[u] + du
            if alt < dist[v]:
                dist[v] = alt
                pq.put((alt, v))
    return dist


n, m, aleg_time = map(int, input().strip().split())
g = []
for _ in range(n):
    g.append([])
for _ in range(m):
    u, v, d = map(int, input().strip().split())
    g[u].append((v, d))
    g[v].append((u, d))

dist = dijkstra(g)
res = sum(dist)
if res <= aleg_time:
    print(res)
else:
    print("Aleg, ¡a decorar!")