
def get_best_item(data, candidates):
    best_profit = -1
    best_item = -1
    for c in candidates:
        profit = data['profit'][c]
        if profit > best_profit:
            best_profit = profit
            best_item = c
    return best_item


def greedy_schedule(data):
    n = len(data['profit'])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    last_date = max(data['dead_line'])
    sol = [-1] * (last_date+1)
    j = 0
    while candidates and j <= last_date:
        best_item = get_best_item(data, candidates)
        candidates.remove(best_item)
        i = data['dead_line'][best_item]
        found = False
        while i > 0 and not found:
            if sol[i] == -1:
                sol[i] = best_item
                found = True
            i -= 1
        j += 1
    return sol


data = {
    'profit': [50, 10, 15, 30],
    'dead_line': [2, 1, 2, 1]
}
schedule = greedy_schedule(data)
print(schedule)