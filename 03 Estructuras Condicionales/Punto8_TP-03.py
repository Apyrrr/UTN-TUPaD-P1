nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")