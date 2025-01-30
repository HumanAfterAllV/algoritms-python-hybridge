##
# 04 - Listas Métodos
# Los métodos mas importantes en listas

import os
os.system("clear")

lista_1 = ["a","b","c","d"] 

lista_1.append("e") #Añade el elemento al FINAL
print(lista_1)

lista_1.insert(0, "@") #Añadimos un elemento en la posición que le indiquemos como primer argumento
print(lista_1)

lista_1.extend(["f", "g", "h"]) #Añade varios elementos al final de la lista
print(lista_1)

lista_1.remove("@") #Eliminar la primera aparición del elemento
print(lista_1)

ultimo = lista_1.pop() #Eliminar el ultimo elemento de la lista 
print(ultimo)
print(lista_1)

lista_1.pop(0) #Eliminar el primer elemento
print(lista_1)

del lista_1[-1] #Elimina un elemento de la lista
print(lista_1)

lista_1.clear() #Elimina TODOS los elementos de la lista
print(lista_1)

lista_2 = [1,2,3,4,5,6,7,8,9]
del lista_2[1:3]
print(lista_2)

numbers = [1,5,7,10,8,15,16,40,3]
numbers.sort()
print(numbers)

print("Ordenando una lista en una nueva lista")
numbers = [1,5,7,10,8,15,16,40,3]
new_numbers = sorted(numbers)
print(numbers, new_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.