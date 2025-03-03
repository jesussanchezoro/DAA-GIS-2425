
def get_best_task(candidates, tasks):
    best_task = 0
    best_task_time = 0x3f3f3f3f
    for c in candidates:
        if tasks[c] < best_task_time:
            best_task_time = tasks[c]
            best_task = c
    return best_task


def order_tasks(tasks):
    candidates = set()
    for i in range(len(tasks)):
        candidates.add(i)
    sol = []
    while candidates:
        best = get_best_task(candidates, tasks)
        candidates.remove(best)
        sol.append(best)
    return sol


def calculate_waiting_time(sol, tasks):
    times = []
    suma = 0
    for i in range(len(sol)):
        task = sol[i]
        suma += tasks[task]
        times.append(suma)
    print(times)
    print(sum(times))


tasks = [5, 10, 3]
sol = order_tasks(tasks)
print(sol)
calculate_waiting_time(sol, tasks)