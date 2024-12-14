import random


numero_secreto = random.randint(1,101)
cantidad_de_intentos = 0
cant_max_intentos = 6
adivinado = False

print("¡Bienvenida al juego de adivinar el número secreto!")

while not adivinado and cantidad_de_intentos < cant_max_intentos:
    entrada = input("Introduce un número del 1 al 100: ") 
    numero = int(entrada)
    if numero == numero_secreto:
        print("Felicitaciones, Júpiter! ganaste")
        adivinado = True
    elif numero < numero_secreto:
        print("el numero es mayor al ingresado")
    else:
        print("el numero es menor al ingresado")

    cantidad_de_intentos += 1

if not cantidad_de_intentos < cant_max_intentos:
    print("Alpiste perdiste, Julieta cara de teta! No adivinaste dentro de los 5 intentos")