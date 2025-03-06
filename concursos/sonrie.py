n = int(input().strip())
familia = []
for _ in range(n):
    nombre, paciencia, urgencia, tiempo = input().strip().split()
    familia.append((nombre, int(paciencia), int(urgencia), int(paciencia) / int(urgencia), int(tiempo)))

orden = []
suma = 0
familia.sort(key = lambda x : x[3])
first_name = "zzzzz"
first_time = -1
for f in familia:
    orden.append((f[0], suma))
    if f[0] < first_name:
        first_name = f[0]
        first_time = suma
    suma += f[4]
    print(f[0])

print(first_time)










