def cifrado(mensaje, desplazamiento): 
    resultado = []

    for letra in mensaje:
        if letra.isalpha():
            base = ord("A") if letra.upper() else ord("a")
            nueva_letra = chr(((ord(letra) - base + desplazamiento) % 26) + ord("A"))
            resultado.append(nueva_letra)
        else:
            resultado.append(letra)
            
    return "".join(resultado)
    
def descifrar(mensaje, desplazamiento):
    
    return cifrado(mensaje, - desplazamiento)


continuar = ""
mensaje = ""
opciones = {
    1: "Cifrar",
    2: "Descifrar",
}

while continuar != "n":
    print("Opciones: ")
    for key, value in opciones.items():
        print(f"{key} - {value}")
    try:
        opcion = abs(int(input("Seleccione una opción: ")))

        if opcion in [1,2]:

            mensaje = str(input("Introduce el mensaje a cifrar: ")).strip()
            desplazamiento = abs(int(input("Introduce el cifrado: ")))
            
            if opcion == 1:
                mensaje_cifrado = cifrado(mensaje, desplazamiento)
                print(f"🔐 Mensaje cifrado: {mensaje_cifrado}")
            else:
                mensaje_descifrado = descifrar(mensaje, desplazamiento)
                print(f"🔓 Mensaje descifrado: {mensaje_descifrado}")
                
        else:
            print("Error: Introduce una opción valida")
    except ValueError:
        print("Error: Introduce una opción valida")
    continuar = str(input("¿Desea continuar? s/n: ")).strip().lower()
    if continuar == "n":
        print("Saliendo del programa")
        break
