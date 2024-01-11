
from prettytable import PrettyTable
from termcolor import colored
from dane import DaneGry
from dane import clear_terminal
from gracz import Gracz
from mechaniki import odpocznij, zjedz, napij_sie

class Akcje:
    def menu_akcji(self):
        while True:
            clear_terminal()
            table = PrettyTable()

            # Dodawanie kolumn do tabeli
            table.field_names = [colored("#", 'cyan'), colored("Akcja", 'cyan')]

            # Dodawanie danych do tabeli
            table.add_row([colored("1", 'yellow'), colored("Odpocznij", 'green')])
            table.add_row([colored("2", 'yellow'), colored("Zjedz", 'yellow')])
            table.add_row([colored("3", 'yellow'), colored("Napij się", 'cyan')])
            table.add_row([colored("4", 'yellow'), colored("Powrót", 'red')])

            # Ustawianie koloru nagłówka
            table.title = colored('Menu Akcji', 'blue')

            # Wyświetlanie tabeli
            print(table)

            wybor = input("Wybierz numer akcji (1-4): ")

            if wybor == '1':
                clear_terminal()
                odpocznij()
            elif wybor == '2':
                clear_terminal()
                zjedz()
            elif wybor == '3':
                clear_terminal()
                napij_sie()
            elif wybor == '4':
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")