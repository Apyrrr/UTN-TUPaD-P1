import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if intento == secreto:
        print("¡Correcto! Lo adivinaste en", intentos, "intentos.")
        break