import time

print("Lanzamiento ha comenzado")
for n in range(15, 0, -1):
    if n % 5 == 0:
        print(f"Advertencia: {n} segundos para el lanzamiento")
        continue
    time.sleep(1)
    print(n)
    if n == 1:
        print("Lanzamiento iniciado")