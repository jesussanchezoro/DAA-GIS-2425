from collections import deque

def topsort(g):
    data = {
        "graph": g,
        "state": dict(),
        "d": dict(),
        "f": dict(),
        "time": 0,
        "list": deque()
    }
    for k in g.keys():
        data['state'][k] = 'NOT_VISITED'
        data['d'][k] = 0
        data['f'][k] = 0

    for k in g.keys():
        if data['state'][k] == "NOT_VISITED":
            top_sort_visit(data, k)
    print(data['list'])

def top_sort_visit(data, k):
    data['state'][k] = "VISITED"
    data['time'] += 1
    data['d'][k] = data['time']
    for adj in data['graph'][k]:
        if data['state'][adj] == "NOT_VISITED":
            top_sort_visit(data, adj)
    data['state'][k] = 'FINISHED'
    data['time'] += 1
    data['f'][k] = data['time']
    data['list'].appendleft(k)




g = {
    "calcetines": ["zapatos"],
    "pantalon": ["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [],
    "cinturon": [],
    "jersey": []
}

topsort(g)