# import random

# num_random = random.randint(0, 9)

# while True:
#     try:
#         num = int(input("Adivina el numero del 0 al 9: "))
#         if num == num_random:
#             print("Has acertado")
#             break
#         else:
#             print("Vuelve a intentarlo")
#     except:
#         print("Introduce un numero del 0 al 9")


texto = str(input("Escribe un texto: ")).lower()
palabras = ["urgente", "importante"]
es_importante = False

for palabra in palabras:
    if palabra in texto:
        es_importante = True
        break
if es_importante and len(texto) > 15:
    print("El texto es importante y largo")
elif es_importante:
    print("El texto es importante")
elif len(texto) > 15:
    print("El texto es largo")
else:
    print("El texto no es importante ni largo")
