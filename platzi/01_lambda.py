numbers = range(11)

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(F"Cuadrados: {squared_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Números pares: {even_numbers}")