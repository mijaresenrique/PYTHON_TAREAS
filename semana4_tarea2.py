N = int(input("Ingrese la cantidad de numeros (N): "))

suma = 0

for i in range(1, N + 1):
    num = int(input(f"Ingrese número {i}: "))
    suma += num

    if i == 1:
        mayor = num
        menor = num
    else:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

promedio = suma / N

print("Cantidad de números:", N)
print("Suma total:", suma)
print("Promedio:", promedio)
print("Mayor:", mayor)
print("Menor:", menor)