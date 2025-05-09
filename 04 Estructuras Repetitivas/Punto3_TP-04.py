a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
inicio = min(a, b) + 1
fin = max(a, b)
suma = sum(range(inicio, fin))
print("La suma es:", suma)