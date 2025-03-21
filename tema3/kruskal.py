
def sort_candidates(g):
    candidates = []
    for adjs in g:
        for (src, dst, w) in adjs:
            candidates.append((w, src, dst))
    candidates.sort()
    return candidates


def update_components(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(g):
    candidates = sort_candidates(g)
    components = list(range(len(g)))
    number_components = len(components)
    sol = 0
    i = 0
    while i < len(candidates) and number_components > 1:
        w, src, dst = candidates[i]
        if components[src] != components[dst]:
            sol += w
            number_components -= 1
            update_components(components, components[src], components[dst])
        i += 1
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

sol = kruskal(g)
print(sol)