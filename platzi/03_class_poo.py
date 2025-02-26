class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")
        
person1 = Person("Ana", 24)

person1.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado ${amount} saldo actual {self.balance}")
        else:
            print("No se puede depositar: Cuenta inactiva")
        