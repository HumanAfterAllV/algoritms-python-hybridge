opcion_deseada = ""

while opcion_deseada != "5":
    print("*************Menú de opciones***********")
    print("1. Saludar")
    print("2. Pedir edad")
    print("3. Sumar 2 números")
    print("4. Restar 2 números")
    print("5. Salir")

    opcion_deseada = input("Dame la opción deseada: ")
    print("==========================")
    
    try:
        if opcion_deseada == "1":
            print("Hola!")
        elif opcion_deseada == "2":
            edad = input("¿Cuál es tu edad?: ")
            print("Tienes", edad, "años.")
        elif opcion_deseada == "3":
            num1 = int(input("Introduzca un número: "))
            num2 = int(input("Introduzca un número: "))
            print("El resultado de", str(num1), " + ", num2, "es", (num1 + num2))
        elif opcion_deseada == "4":
            num1 = int(input("Introduzca un número: "))
            num2 = int(input("Introduzca un número: "))
            print("El resultado de", str(num1), " - ", num2, "es", (num1 - num2))
        elif opcion_deseada == "5":
            print("Saliendo del programa...")
        else:
            print("Opción no válida, por favor intenta de nuevo.")
        
        continuar = str(input("Deseas continuar? s/n: ")).strip().lower()
        if continuar == "n":
            print("Saliendo del programa")
            break
        else:
            continue
    except ValueError:
        print("Error: Por favor, introduce un número válido.")