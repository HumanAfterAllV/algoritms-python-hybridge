#cuenta = float(input("Ingresa la cuenta: "))
#propina = float(input("Ingresa la propina: "))

#resultado = (cuenta * propina) / 100 + cuenta

#print("Total: \n", resultado)

#base = 10
#altura = 5

#print(float(base * altura) / 2)

#print(int(10 / 3))

#x = 5

#x = x + 3
#print(x)

value_1 = float(input("Valor 1: "))
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
