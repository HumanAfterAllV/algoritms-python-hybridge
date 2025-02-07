# valor_1 = int(input("Ingresa el valor 1: "))
# valor_2 = int(input("Ingresa el valor 2: "))

# valor_1 = abs(valor_1)
# valor_2 = abs(valor_2)

# ud_1 = valor_1 % 10
# ud_2 = valor_2 % 10

# if ud_1 == ud_2:
#     print("El ultimo dígito es igual")
# else:
#     print("No es igual el ultimo dígito")



# num = int(input("Escribe un numero: "))
# cd = 0

# while num != 0:
#     num = num // 10
#     cd += 1
    
# print(f"El numero tiene {cd} dígitos")



# num = int(input("Escribe un numero del 1 al 5: "))
# lista = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco"]

# num = abs(num)

# if num <= 5:
#     print(lista[num])
# else:
#     print("Numero equivocado")


# num = int(input("Escribe un numero: "))

# if num <= 100:
#     primo = num // num
#     if primo == num or 1:
#         print("Es un numero primo")
#     else:
#         print("No es primo")
# else:
#     print("No es menor que 100")


# num = int(input("Escribe un numero: "))

# num = abs(num)

# if num % 4 == 0 :
#     print(num / 2)
# if num % 5 == 0:
#     print(num * num)
# if num % 6 == 0:
#     while num >= 10 :
#         num = num // 10
#     print(num)



num = abs(int(input("Escribe un numero: ")))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)

