#Operadores lógicos/comparación

name = str(input("¿Cual es tu nombre completo?: "))
age = int(input("¿Cual es tu edad?: "))

if(age >= 18) :
    print(f"Eres mayor de edad, puedes votar {name}")
else:
    print(f"Aun no tienes el permiso para votar {name}")

