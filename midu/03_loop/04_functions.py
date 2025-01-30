##
# 04_ funciones
# Bloques de código reutilizablez y parametrizables para hacer tareas especificas
##

# def saludar():
#     print("Hola")

# saludar()

# def saludar_a(name: str):
#     print(f"Hola {name}")

# saludar_a("Israel")

#Funciones con más parámetros
# def sumar(a, b: int):
#     suma = a + b
#     return suma

# result = sumar(2, 4)
# print(result)


#Descripción mas explicita en funciones
# def restar(a, b):
#     """Resta dos números y devuelve el resultado"""
#     return a-b

# help(restar)

#Parámetros por defecto
# def multiplicar(a, b =5):
#     return a * b

# print(multiplicar(2, 3))
# print(multiplicar(2))

#Argumentos por clave
def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy {nombre}, tengo {edad} años y soy {sexo}")

describir_persona("Israel", 30, "hombre")

describir_persona(edad=30, nombre="Erandi", sexo="mujer")


#Parámetros arbitrarios
def sumar_numeros(*numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora