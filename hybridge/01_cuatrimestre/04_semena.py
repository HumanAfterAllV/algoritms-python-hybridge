def invert_string(s):
    return "".join(reversed(s))

word = str(input("Escribe una palabra: "))
print(invert_string(word))




color = str(input("Escribe un color del semáforo(verde/rojo): ")).lower()

if(color == "verde"):
    print("Cambia a rojo")
elif(color == "rojo"):
    print("Cambia el color a verde")
else:
    print("El color es incorrecto")




movie = int(input("¿Cual es tu genero favorito?: \n 1.-Comedia \n 2.-Terror"))

if(movie == 1):
    print("Superbad")
elif(movie == 2):
    print("El conjuro")
else:
    print("Error de opción")





pet = str(input("Ingresa si tienes (perro/gato): ")).lower()
age_pet = int(input("Cuantos años tiene tu mascota?: "))

text = f"Tu {pet} tiene años humanos: " 

if(pet == "perro"):
    print(text, age_pet * 7)
elif(pet == "gato"):
    print(text, age_pet * 5)