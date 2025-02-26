caracteres = str(input("Escribe un caracter: "))
ascii_values = []

suma = 0

for caracter in caracteres:
    ascii_values.append(ord(caracter))

for valor in ascii_values:
    suma += valor

print(suma)