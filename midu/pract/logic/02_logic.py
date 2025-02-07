"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, 
la suma de todos los números pares en la lista).

"""

def jurassic_par(lista_huevos):
    
    pares = [huevo for huevo in lista_huevos if huevo % 2 == 0]
    suma = 0

    for par in pares:
        suma += par
    return print(f"La lista de pares es: {pares} y la suma es {suma}")

print(jurassic_par([1,8,10,11,13,24,52,68,95,77,190]))