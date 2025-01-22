# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

list_1 = [1,2,3,4,5]

list_1.append(6)
print(list_1)

list_1.insert(2, 10)
print(list_1)

list_1.pop(0) and list_1.insert(0, 0)
print(list_1)