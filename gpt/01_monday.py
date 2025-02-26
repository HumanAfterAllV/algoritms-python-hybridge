#RETO FIZZBUZZ

for n in range(1, 101):
    resultado = ""

    if n % 3 == 0:
        resultado += "Fizz"
    if n % 5 == 0:
        resultado += "Buzz"
    print(resultado if resultado else n)

#RETO PERSONA

lista_nombres = [
    { "nombre": "Juan", "edad": 20},
    { "nombre": "Sebastian", "edad": 22},
    { "nombre": "Maria", "edad": 17},
    { "nombre": "Roberto", "edad": 25},
]

#RETO BUSQUEDA

mayores_edad = [persona["nombre"] for persona in lista_nombres if persona["edad"] >= 18]
print(f"Personas mayores de edad: {mayores_edad}")


palabras = ["Comedor", "Cocina", "Sala", "Recamara", "Comedor"]

print(palabras.count("Comedor"))