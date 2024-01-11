#Mateusz
import tqdm as loading
import time
import random as r
from dane import clear_terminal
from prettytable import PrettyTable  # Instaluj: pip install prettytable
from termcolor import colored  # Instaluj: pip install termcolor
from dane import DaneGry
from gracz import Gracz

dane_gry = DaneGry()

def fishing_process():
        fishing_time=r.randrange(2,15)
        loading_time=fishing_time*5
        time.sleep(fishing_time)
        for i in loading(range(loading_time), desc='Trwa wędkowanie'):
            time.sleep(0.2)
        print(colored('Złowiłeś rybę!', 'yellow'))

def fishing():
    while True:
        fishing_rozpocznij = input(colored('F aby zarzucić wędkę'))
        if fishing_rozpocznij == 'f'or'F':
            fishing_process()
        else:
            break

class Fishing:
    def menu_fishing():
        while True:
            table = PrettyTable()
            # Dodawanie kolumn do tabeli
            table.field_names = [colored("#", 'cyan'), colored("Opcja", 'cyan')]

            # Dodawanie danych do tabeli
            table.add_row([colored("1", 'yellow'), colored("Zacznij lowic", 'green')])
            table.add_row([colored("2", 'yellow'), colored("Wyswietl ryby w eq", 'yellow')])
            table.add_row([colored("3", 'yellow'), colored("Wyjście", 'red')])

            # Ustawianie koloru nagłówka
            table.title = colored('=== Menu wędkowania ===', 'blue')

            # Wyświetlanie tabeli
            print(table)

            wybor_fishing = input("Wybierz opcję: ")

            if wybor_fishing == "1":
                fishing()
            elif wybor_fishing == "2":
                pass
            elif wybor_fishing == "3":
                clear_terminal()
                break              
            else:
                print("Niepoprawny wybór. Spróbuj ponownie.")
