# 1) Lista de múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

# 2) Lista con 5 elementos y mostrar el penúltimo
gustos = ["pizza", "videojuegos", "música", "leer", "viajar"]
print("Penúltimo elemento:", gustos[-2])

# 3) Crear lista vacía y agregar tres palabras con append
lista_vacia = []
lista_vacia.append("manzana")
lista_vacia.append("banana")
lista_vacia.append("pera")
print(lista_vacia)

# 4) Reemplazar elementos en la lista 'animales'
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# 5) Este programa elimina el valor más alto de una lista de números.

# 6) Lista con números del 10 al 30 saltando de 5 en 5, mostrar los dos primeros
lista_saltos = list(range(10, 31, 5))
print("Dos primeros elementos:", lista_saltos[:2])

# 7) Reemplazar elementos centrales en la lista "autos"
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print(autos)

# 8) Crear lista "dobles" con el doble de 5, 10 y 15 usando append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# 9) Modificar lista de listas 'compras'
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")  # Agregar "jugo" al tercer cliente
compras[1][1] = "tallarines"  # Reemplazar "fideos" por "tallarines"
compras[0].remove("pan")  # Eliminar "pan" del primer cliente
print(compras)

# 10) Crear lista anidada con valores específicos
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)
