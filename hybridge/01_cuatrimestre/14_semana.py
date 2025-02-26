import random
import time

options = {
    1: "Adivina el numero",
    2: "Lanzamiento de cohete"
}

def ale_number():
    print("Adivina el numero del 0 al 10")
    number_ale = random.randint(0,10)
    n = -1

    while n != number_ale:
        try:
            n = abs(int(input("Adivina el numero aleatorio: ")))
            if n == number_ale:
                print(f"Numero adivinado {number_ale}")
                break
            else:
                print("Sigue intentando")
        except ValueError:
            print("Opción invalida, escribe un numero entero")

def launch():
    print("Lanzamiento iniciado")
    for n in range(10, 0, -1):
        time.sleep(1)
        print(n)
    print("Lanzamiento iniciado")

continuar = ""

while continuar != "n":
    print("Opciones disponibles")
    for key, value in options.items():
        print(f"{key} - {value}")

    try:
        respuesta = abs(int(input("Selecciona una opción: ")))
        if respuesta == 1:
            ale_number()
        if respuesta == 2:
            launch()
        else:
            print("Opción no valida")
        continuar = str(input("Desea continuar s/n?: ")).strip().lower()
        if continuar not in ["s", "n"]:
            print("Entrada no valida, por favor ingrese una opción valida")
            continuar = str(input("Desea continuar s/n?: ")).strip().lower()
        if continuar == "n":
            print("Saliendo del programa")
            break
    except ValueError:
        print("Error: Por favor, introduce una opción valida")