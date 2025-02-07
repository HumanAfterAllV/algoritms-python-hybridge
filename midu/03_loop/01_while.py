print("\n Bucle while")

contador = 0

while contador <= 5:
    print(contador)
    contador += 1


print("\n Bucle while con break")
contador = 0

while True:
    print(contador)
    contador += 1
    if (contador == 5):
        break

#continue
print("\n Bucle con continue")
contador = 0
while contador < 10:
    contador += 1
    if(contador % 2 == 0):
        continue

    print(contador)


#else, esta condición cuando se ejecuta
print("\n Bucle while con else")
contador = 0

while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle a terminado")

#pedir al usuario un numero que tiene
#que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
    numero = int(input("Escribe un numero positivo")) 
    if(numero < 0):
        print("El numero debe ser positivo")
print(f"El numero que has introducido es {numero}")

#pedir al usuario un numero que tiene
#que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo")) 
        if(numero < 0):
            print("El numero debe ser positivo")
    except:
        print("Introduce un numero positivo")
print(f"El numero que has introducido es {numero}")

# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")