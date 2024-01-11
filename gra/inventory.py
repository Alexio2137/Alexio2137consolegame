#Wojtek

from prettytable import PrettyTable
from termcolor import colored
from dane import DaneGry
from dane import clear_terminal

class Inventory:
    def inventory_menu():
        while True:
            table = PrettyTable()

            table.field_names = [colored("#", "cyan"), colored("Nazwa", "cyan")]

            table.add_row([colored("1", 'yellow'), colored("Wyświetl menu", 'yellow')])
            table.add_row([colored("2", 'yellow'), colored("Nałóż item", 'green')])
            table.add_row([colored("3", 'yellow'), colored("Zdejmij item", 'blue')])
            table.add_row([colored("4", 'yellow'), colored("Wyrzuć item", 'magenta')])
            table.add_row([colored("5", 'yellow'), colored("Powrót", 'red')])
            print(table)
            wybor_inventory_menu = input("Wybór: ")

            if wybor_inventory_menu == '5':
                clear_terminal()
                break
            
    # Do naprawy krecie!
    # def inventory():
        while True:
            table = PrettyTable()
        
            # Dodawanie kolumn do tabeli
            table.field_names = [colored("#", 'cyan'), colored("Rodzaj", 'cyan'), colored("Nazwa", 'cyan'), colored("Ilość", 'cyan')]

            # Dodawanie danych do tabeli
            table.add_row([colored("1", 'yellow'), colored("Hełmy", 'red')])
            table.add_row([colored("2", 'yellow'), colored("Zbroje", 'orange')])
            table.add_row([colored("3", 'yellow'), colored("Buty", 'yellow')])
            table.add_row([colored("4", 'yellow'), colored("Rękawice", 'green')])
            table.add_row([colored("5", 'yellow'), colored("Bronie", 'blue')])
            table.add_row([colored("6", 'yellow'), colored("Narzędzia", 'purple')])
            table.add_row([colored("7", 'yellow'), colored("Potki leczące", 'pink')])
            table.add_row([colored("8", 'yellow'), colored("Potki zwiększające ap", 'red')])
            table.add_row([colored("9", 'yellow'), colored("Potki zwiększające dp", 'orange')])
            table.add_row([colored("10", 'yellow'), colored("Potki odnawiające energie", 'yellow')])
            table.add_row([colored("11", 'yellow'), colored("Picia", 'green')])
            table.add_row([colored("12", 'yellow'), colored("Jedzenia", 'blue')])
            table.add_row([colored("13", 'yellow'), colored("Looty", 'purple')])
            table.add_row([colored("14", 'yellow'), colored("Potki odnawiające energie", 'pink')])
            table.add_row([colored("15", 'yellow'), colored("Stajnia", 'red')])
            table.add_row([colored("16", 'yellow'), colored("Inne", 'orange')])
            table.add_row([colored("17", 'yellow'), colored("Powrót", 'yellow')])

            print(table)