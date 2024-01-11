#Aleks

from podroze.podroz_do_krainy import PodrozDoKrainy
from walka import Walka
from prettytable import PrettyTable  # Instaluj: pip install prettytable
from termcolor import colored  # Instaluj: pip install termcolor
from gracz import Gracz
from dane import DaneGry
from Akcje import Akcje
from dane import clear_terminal

dane_gry = DaneGry()
# Wywołanie metody lokalizacje, która utworzy atrybut krainy
dane_gry.lokalizacje()


class Podroz:
    @staticmethod
    def menu_podrozy(gracz):
        while True:
            clear_terminal()
            table = PrettyTable(['Atrybut', 'Wartość'])
            table.add_row(['Punkty życia (HP)', colored(str(gracz.hp), 'red')])
            table.add_row(['Poziom wytrzymałości', colored(str(gracz.stamina), 'green')])
            table.add_row(['Poziom energii', colored(str(gracz.energia), 'red')])
            table.add_row(['Poziom głodu', colored(str(gracz.effekty['glod']), 'red')])
            table.add_row(['Poziom napojenia', colored(str(gracz.effekty['pragnienie']), 'red')])
            
            table_options = PrettyTable(['#', colored('Opcja', 'cyan')])
            table_options.add_row([colored('1', 'yellow'), colored('Pokaż menu Gracza', 'green')])
            table_options.add_row([colored('2', 'yellow'), colored('Przejdź do menu akcji', 'yellow')])
            table_options.add_row([colored('3', 'yellow'), colored('Podróżuj do krainy ...', 'yellow')])
            table_options.add_row([colored('4', 'yellow'), colored('Użyj mapy', 'yellow')])
            table_options.add_row([colored('5', 'yellow'), colored('Losowa podróż', 'yellow')])
            table_options.add_row([colored('6', 'yellow'), colored('Powrót', 'yellow')])
            
            print(colored('=== Menu Podróży ===', 'blue'))
            print(table)
            print(table_options)

            wybor_opcji_podrozy = input('Podaj swój wybór: ')

            if wybor_opcji_podrozy == '1':
                clear_terminal()
                Gracz.menu_gracza(gracz)
            elif wybor_opcji_podrozy == '2':
                clear_terminal()
                Akcje.menu_akcji(gracz)
            elif wybor_opcji_podrozy == '3':
                clear_terminal()
                # Utwórz instancję klasy z innego folderu
                podroz_instance = PodrozDoKrainy()
                # Wywołaj metodę na instancji
                podroz_instance.menu_wyboru_krainy(dane_gry)
                
            elif wybor_opcji_podrozy == '4':
                clear_terminal()
                # Tutaj dodaj logikę dla opcji 4 - Użyj mapy
                pass
            elif wybor_opcji_podrozy == '5':
                clear_terminal()
                # Tutaj dodaj logikę dla opcji 5 - Losowa podróż
                pass
            elif wybor_opcji_podrozy == '6':
                clear_terminal()
                break
            else:
                print(colored('Nieprawidłowy wybór. Spróbuj ponownie.', 'red'))