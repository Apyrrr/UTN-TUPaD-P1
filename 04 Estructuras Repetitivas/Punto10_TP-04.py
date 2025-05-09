numero = input("Ingrese un número entero: ")
invertido = numero[::-1] if numero[0] != '-' else '-' + numero[:0:-1]
print("Número invertido:", invertido)