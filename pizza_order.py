import csv
import datetime
import os

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Klasik(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
        self.cost = 20.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class Margarita(Pizza):
    def __init__(self):
        self.description = "Margarita Pizza"
        self.cost = 30.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turk Pizza"
        self.cost = 45.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class SadePizza(Pizza):
    def __init__(self):
        self.description = "Sade Pizza"
        self.cost = 15.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

class Zeytin(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Zeytin"
        self.cost = 4.0

class Mantarlar(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Mantarlar"
        self.cost = 6.0

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Keci Peyniri"
        self.cost = 8.0

class Et(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Et"
        self.cost = 10.0

class Sogan(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Sogan"
        self.cost = 3.0

class Misir(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Misir"
        self.cost = 7.0

def main():
    f = open('Menu.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()


    pizza = None
    while not pizza:
        try:
            choice = int(input("Please select a pizza: "))
            if choice == 1:
                pizza = Klasik()
            elif choice == 2:
                pizza = Margarita()
            elif choice == 3:
                pizza = TurkPizza()
            elif choice == 4:
                pizza = SadePizza()
        except ValueError:
            continue

    while True:
        try:
            choice = int(input("Please choose a sauce (enter 0 to finish selection): "))
            if choice == 0:
                break
            elif choice == 11:
                pizza = Zeytin(pizza)
            elif choice == 12:
                pizza = Mantarlar(pizza)
            elif choice == 13:
                pizza = KeciPeyniri(pizza)
            elif choice == 14:
                pizza = Et(pizza)
            elif choice == 15:
                pizza = Sogan(pizza)
            elif choice == 16:
                pizza = Misir(pizza)
            else:
                print("You have made an invalid choice. Please try again.")
        except ValueError:
            print("You have entered an invalid entry. Please enter numbers only.")
            continue

    print("Total price:", pizza.get_cost())

    name = input("Please enter your name: ")
    while True:
        tc = input("Please enter your TR ID number: ")
        if tc.isdigit() and len(tc) == 11:
            break
        else:
            print("Invalid TR ID number. Please enter an 11-digit number.")

    card_number = input("Please enter your credit card number: ")
    
    while True:
        card_cvv = input("Please enter your credit card CVV number: ")
        if card_cvv.isdigit() and len(card_cvv) == 3:
            break
        else:
            print("Invalid credit card CVV number. Please enter a 3-digit number.")

    now = datetime.datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    with open('Orders_Database.csv', mode='a', newline='') as orders_file:
        fieldnames = ['Pizza','Cost', 'Name', 'TC', 'Card Number', 'Order Time', 'Card CVV']
        writer = csv.DictWriter(orders_file, fieldnames=fieldnames)
        if os.stat("Orders_Database.csv").st_size == 0:
            writer.writerow({'Pizza': fieldnames[0],'Cost': fieldnames[1], 'Name': fieldnames[2], 'TC': fieldnames[3], 'Card Number': fieldnames[4], 'Order Time': fieldnames[5], 'Card CVV': fieldnames[6]})
        writer.writerow({'Pizza': pizza.get_description(),'Cost': pizza.get_cost(), 'Name': name, 'TC': tc, 'Card Number': card_number, 'Order Time': current_time, 'Card CVV': card_cvv})

if __name__ == "__main__":
    main()