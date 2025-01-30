# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales


""" num = float(input("Primer numero: "))
num_2 = float(input("Segundo numero: "))

comparacion = "Primer numero es mayor" if num > num_2 else "Segundo numero es mayor"
print(comparacion) """

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

""" value_1 = float(input("Valor 1: "))
value_2 = float(input("Valor 2: "))

option =  int(input("Operación a realizar: \n 1.-Suma \n 2.- Resta \n 3.-Multiplicación \n 4.-División \n Opción: " ))

match option:
    case 1:
        print(value_1 + value_2)
    case 2:
        print(value_1 - value_2)
    case 3:
        print(value_1 * value_2)
    case 4:
        if(value_2 != 0):
            print(f"{value_1 / value_2 } residuo:{value_1 % value_2}")
        else:
            print("No se puede dividir entre 0")
    case _:
        print("Error escogiendo opción")

 """
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

""" year = int(input("Escribe un año: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")
 """

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("Escribe tu edad: "))

if(age <= 2):
    print("Bebe")
elif(age >= 3 and age <= 12):
    print("Niño")
elif(age >= 13 and age <= 17):
    print("Adolescente")
elif(age >= 18 and age <= 64):
    print("Adulto")
elif(age >= 65 ):
    print("Adulto mayor")