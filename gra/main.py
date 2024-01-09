# Importujemy klasy DaneGry, Gracz, inventory, fishing, mechaniki, akcje, podroz i Osada z odpowiednich plików
from prettytable import PrettyTable  # Instaluj: pip install prettytable
from termcolor import colored  # Instaluj: pip install termcolor
from dane import DaneGry
from gracz import Gracz
from osada import Osada
from inventory import inventory
from fishing import fishing
from podroz import podroz
from Akcje import akcje
from mechaniki import mechaniki
from enchanty import enchanty

# Funkcja tworząca nowego gracza i dokonująca przykładowego zakupu hełmu
def stworz_nowego_gracza(dane_gry):
    while True:
        imie = input("Podaj imię gracza: ")
        if imie.strip():
            break
        else:
            print("Imię nie może być puste. Spróbuj ponownie.")

    nowy_gracz = Gracz(imie)
    return nowy_gracz

# Główna pętla gry
nowy_gracz = stworz_nowego_gracza(DaneGry())  

while nowy_gracz.hp > 0:
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
        podroz.menu_podrozy(nowy_gracz)  # Załóżmy, że istnieje funkcja menu_podrozy w module podroz
    elif wybor == "3":
        akcje.menu_akcji(nowy_gracz)  # Załóżmy, że istnieje funkcja menu_akcji w module akcje
    elif wybor == "4":
        print("Dziękujemy za grę. Do zobaczenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
