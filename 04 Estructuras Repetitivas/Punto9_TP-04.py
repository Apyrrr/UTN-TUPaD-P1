cantidad = 100
suma = 0
for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
media = suma / cantidad
print("La media es:", media)