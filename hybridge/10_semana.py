items = []
respuesta = ""

tesoros = {
    1: "Brújula",
    2: "Cuchillo",
    3: "Cantimplora",
    4: "Mochila"
}
while respuesta != "n":
    print("Tesoros disponibles")
    for key, value in tesoros.items():
        print(f"{key} - {value}")

    try:
        respuesta = abs(int(input("Que items deseas llevar: ")))
        if respuesta in tesoros:
            items.append(tesoros[respuesta])
        else:
            print("Opción no valida, intenta de nuevo.")
        continuar = str(input("Deseas agregar mas cosas s/n?: ")).strip().lower()
        if continuar == "n":
            print("Saliendo del programa")
            break
        else:
            continue
    except ValueError:
        print("Error: Por favor, introduce un opción valida")

print("Items seleccionado:", items)