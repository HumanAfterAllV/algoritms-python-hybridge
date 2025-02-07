def contar_vocales (texto):

    texto =texto.lower()

    vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}

    for letra in texto:

        if letra in vocales:

            vocales [letra] += 1

    return vocales

entrada = input("Ingrese un texto: ")

resultado = contar_vocales(entrada)

print("Frecuencia de vocales:", resultado)

