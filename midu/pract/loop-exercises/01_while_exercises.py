# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

contador = 10

while contador >= 1:
    print(contador)
    contador = contador - 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

numero = 2
suma = 0

while numero <= 21:
    suma += numero
    numero += 2

print(suma)



# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

factorial = 1
numero = -1

while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
        if numero < 0:
            print("El numero debe ser positivo")
        else:
            for i in range(1, numero + 1):
                factorial *= i
    except ValueError:
        print("Introduce un numero positivo")
print(factorial)


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

pass_len = 0

while pass_len < 8:
    try:
        pass_len = len(str(input("Introduce una contraseña de 8 caracteres: ")))
        if pass_len <= 7:
            print("Introduce una contraseña valida")
        else:
            print("Contraseña valida")
    except ValueError:
        print("Introduce una contraseña valida")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.


numero = int(input("Introduce un numero: "))
multi = 1

while multi <= 10:
    resultado = numero * multi
    print(f"{numero}x{multi} = {resultado}")
    multi += 1



# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.


numero =  int(input("Introduce un numero positivo: "))
n = 2

while n <= numero:
    primo = True
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            primo == False
            break
        divisor += 1
    if primo:
        print(n)
    n += 1