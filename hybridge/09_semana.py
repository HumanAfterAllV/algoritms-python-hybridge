import random

numero_aleatorio = random.randint(0, 9)
numero = -1

while numero !=  numero_aleatorio:
    try:
        numero = abs(int(input("Adivina el numero secreto del 0 al 9: ")))
        if numero < numero_aleatorio:
            print("El numero es menor")
        elif numero > numero_aleatorio:
            print("El numero es mayor")
        elif numero == numero_aleatorio:
            print(f"¡Felicidades! ¡Has adivinado el número secreto! el numero secreto era {numero_aleatorio}")
        else:
            print("Error")
    except ValueError:
        print("Opcion invalida, escribe un numero entero")