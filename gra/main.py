# Importujemy klasy DaneGry, Gracz, inventory, fishing, mechaniki, akcje, podroz i Osada z odpowiednich plików
from prettytable import PrettyTable  # Instaluj: pip install prettytable
from termcolor import colored  # Instaluj: pip install termcolor
from dane import DaneGry
from dane import clear_terminal
from gracz import Gracz
from osada import Osada
from inventory import Inventory
from fishing import Fishing
from podroz import Podroz
from Akcje import Akcje
from enchanty import Enchanty

def stworz_nowego_gracza(dane_gry):
    while True:
        imie = input("Podaj imię gracza: ")
        if imie.strip():
            break
        else:
            print("Imię nie może być puste. Spróbuj ponownie.")

    nowy_gracz = Gracz(imie)
    return nowy_gracz

nowy_gracz = stworz_nowego_gracza(DaneGry())  

while nowy_gracz.hp > 0:
    clear_terminal()
    table = PrettyTable()
    # Dodawanie kolumn do tabeli
    table.field_names = [colored("#", 'cyan'), colored("Opcja", 'cyan')]

    # Dodawanie danych do tabeli
    table.add_row([colored("1", 'yellow'), colored("Gracz", 'green')])
    table.add_row([colored("2", 'yellow'), colored("Podróże", 'yellow')])
    table.add_row([colored("3", 'yellow'), colored("Akcje", 'cyan')])
    table.add_row([colored("4", 'yellow'), colored("Wyjście", 'red')])

    # Ustawianie koloru nagłówka
    table.title = colored('=== Główne Menu ===', 'blue')

    # Wyświetlanie tabeli
    print(table)

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nowy_gracz.menu_gracza()
    elif wybor == "2":
        Podroz.menu_podrozy(nowy_gracz)  
    elif wybor == "3":
        Akcje.menu_akcji(nowy_gracz)  
    elif wybor == "4":
        print("Dziękujemy za grę. Do zobaczenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")