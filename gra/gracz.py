#Aleks, Wojtek i Mateusz

from dane import clear_terminal
from dane import dane_gry
from prettytable import PrettyTable  # Instaluj: pip install prettytable
from termcolor import colored  # Instaluj: pip install termcolor


class Gracz:
    def __init__(self, imie):
        # Informacje o graczu
        self.imie = imie
        self.hp = 100  # Punkty życia
        self.ap = 50  # Punkty ataku
        self.bonus_ap = 0  # Bonus do punktów ataku
        self.dp = 30  # Punkty obrony
        self.bonus_dp = 0  # Bonus do punktów obrony
        self.stamina = 100  # Poziom wytrzymałości
        self.energia = 100  # Poziom energii
        self.coiny = 0  # Ilość monet
        self.effekty = {
            'glod': 50,
            'maxglod': 100,
            'pragnienie': 30,
            'maxpragnienie': 60,
            'zatrucie_potka': 0,
            'max_zatrucie_potka': 50,
        }
        self.mapa = {
            'miasta': [],
            'wsie': [],
            'osady': [],
            'obozy': []
            # Struktura mapy z osadami, miastami, wsiami, obozami
        }
        self.skile = {
            'dodatkowe_ataki': [],
            'dodatkowe_obrony': [],
            'zaklecia': []
            # Umiejętności: dodatkowe ataki, obrony, zaklęcia
        }
        self.poziomy = {
            'lvl': 1,  # Poziom doświadczenia
            'xp': 0,  # Punkty doświadczenia
            'tradelvl': 1,  # Poziom handlu
            'tradexp': 0,  # Punkty doświadczenia w handlu
            'fishlvl': 1,  # Poziom łowienia
            'fishxp': 0,  # Punkty doświadczenia w łowieniu
            'battlelvl': 1, # Poziom walki
            'battlexp': 0 # Punkty doświadczenia w walce
            # Inne poziomy, jeśli są potrzebne
        }
        self.wyposazenie = {
            'helm': None,  # Hełm
            'zbroja': None,  # Zbroja
            'buty': None,  # Buty
            'rekawice': None,  # Rękawice
            'bron':None,     #miecz
            'tarcza': None,    #tarcza
            'bron_dodatkowa': None,  # Dodatkowa broń
            'kon': None,  # Koń
            'tools': None #narzędzia
            # Inne sloty wyposażenia, jeśli są potrzebne
        }
        self.eq_informacje = {
            'sloty': 0,
            'maxsloty': 20,
            'bonussloty': 0,
            'obciarzenie': 0,
            'maxobciazenie': 20,
            'bonusobciazenie': 0
        }
        self.inventory = {
            
        }

    def menu_gracza(self):
        while True:
            clear_terminal()
            table = PrettyTable()
        
            # Dodawanie kolumn do tabeli
            table.field_names = [colored("#", 'cyan'), colored("Opcja", 'cyan')]

            # Dodawanie danych do tabeli
            table.add_row([colored("1", 'yellow'), colored("Informacje o graczu", 'green')])
            table.add_row([colored("2", 'yellow'), colored("Skile", 'yellow')])
            table.add_row([colored("3", 'yellow'), colored("Poziomy", 'cyan')])
            table.add_row([colored("4", 'yellow'), colored("Wyposażenie", 'magenta')])
            table.add_row([colored("5", 'yellow'), colored("Inventory informacje", 'blue')])
            table.add_row([colored("6", 'yellow'), colored("effekty", 'red')])
            table.add_row([colored("7", 'yellow'), colored("Powrót", 'red')])

            # Ustawianie koloru nagłówka
            table.title = colored(' Menu Gracza ', 'blue')

            # Wyświetlanie tabeli
            print(table)

            menu_gracza_wybor = input('Wybierz opcję: ')

            if menu_gracza_wybor == '1':
                clear_terminal()
                self.informacje_o_graczu()
            elif menu_gracza_wybor == '2':
                clear_terminal()
                self.skile_gracza()
            elif menu_gracza_wybor == '3':
                clear_terminal()
                self.poziomy_gracza()
            elif menu_gracza_wybor == '4':
                clear_terminal()
                self.wyposazenie_gracza()
            elif menu_gracza_wybor == '5':
                clear_terminal()
                self.inventory_informacje()
            elif menu_gracza_wybor == '6':
                clear_terminal()
                self.wyswietl_effekty()
                clear_terminal()
            elif menu_gracza_wybor == '7':
                clear_terminal()
                break
            else:
                print(colored('Nieprawidłowy wybór. Spróbuj ponownie.', 'red'))

    def informacje_o_graczu(self):
        table = PrettyTable(['Atrybut', 'Wartość'])
        table.add_row(['Imię', colored(self.imie, 'cyan')])
        table.add_row(['Punkty życia (HP)', colored(str(self.hp), 'red')])
        table.add_row(['Punkty ataku (AP)', colored(str(self.ap + self.bonus_ap), 'yellow')])
        table.add_row(['Punkty obrony (DP)', colored(str(self.dp + self.bonus_dp), 'yellow')])
        table.add_row(['Poziom wytrzymałości', colored(str(self.stamina), 'green')])
        table.add_row(['Poziom energii', colored(str(self.energia), 'green')])
        table.add_row(['Ilość monet', colored(str(self.coiny), 'yellow')])

        print(colored('**** Informacje o Graczu ****', 'green'))
        print(table)
        print(" ")
        stop = input('naciśnij enter aby powrócić: ')
        clear_terminal()

    def skile_gracza(self):
        table = PrettyTable(['Rodzaj umiejętności', 'Lista umiejętności'])
        table.add_row(['Dodatkowe ataki', colored(', '.join(self.skile['dodatkowe_ataki']), 'yellow')])
        table.add_row(['Dodatkowe obrony', colored(', '.join(self.skile['dodatkowe_obrony']), 'yellow')])
        table.add_row(['Zaklęcia', colored(', '.join(self.skile['zaklecia']), 'yellow')])

        print(colored('**** Umiejętności Gracza ****', 'yellow'))
        print(table)
        print(" ")
        stop = input('naciśnij enter aby powrócić: ')
        clear_terminal()

    def poziomy_gracza(self):
        table = PrettyTable(['Typ poziomu', 'Poziom', 'Punkty doświadczenia'])
        table.add_row(['Doświadczenie ogólne (lvl)', colored(str(self.poziomy['lvl']), 'cyan'), colored(str(self.poziomy['xp']), 'cyan')])
        table.add_row(['Handel', colored(str(self.poziomy['tradelvl']), 'cyan'), colored(str(self.poziomy['tradexp']), 'cyan')])
        table.add_row(['Łowienie', colored(str(self.poziomy['fishlvl']), 'cyan'), colored(str(self.poziomy['fishxp']), 'cyan')])
        table.add_row(['Walka', colored(str(self.poziomy['battlelvl']), 'cyan'), colored(str(self.poziomy['battlexp']), 'cyan')])

        print(colored('**** Poziomy Gracza ****', 'cyan'))
        print(table)
        print(" ")
        stop = input('naciśnij enter aby powrócić: ')
        clear_terminal()

    def wyposazenie_gracza(self):
        table = PrettyTable(['Slot wyposażenia', 'Przedmiot'])
        for slot, przedmiot in self.wyposazenie.items():
            table.add_row([colored(slot.capitalize(), 'magenta'), colored(przedmiot if przedmiot else '-', 'magenta')])

        print(colored('**** Wyposażenie Gracza ****', 'magenta'))
        print(table)
        print(" ")
        stop = input('naciśnij enter aby powrócić: ')
        clear_terminal()

    def inventory_informacje(self):
        table = PrettyTable(['Informacje o Ekwipunku', 'Wartość'])
        table.add_row([colored('Liczba slotów', 'blue'), colored(f"{self.eq_informacje['sloty']} / {self.eq_informacje['maxsloty']}", 'blue')])
        table.add_row([colored('Bonus slotów', 'blue'), colored(str(self.eq_informacje['bonussloty']), 'blue')])
        table.add_row([colored('Obciążenie', 'blue'), colored(f"{self.eq_informacje['obciarzenie']} / {self.eq_informacje['maxobciazenie']}", 'blue')])
        table.add_row([colored('Bonus obciążenia', 'blue'), colored(str(self.eq_informacje['bonusobciazenie']), 'blue')])

        print(colored('**** Informacje o Ekwipunku ****', 'blue'))
        print(table)
        print(" ")
        stop = input('naciśnij enter aby powrócić: ')
        clear_terminal()

    def wyswietl_effekty(self):
        table = PrettyTable(['Efekt', 'Wartość'])
        for efekt, wartosc in self.effekty.items():
            table.add_row([colored(efekt.capitalize(), 'red'), colored(str(wartosc), 'red')])

        print(colored('**** Efekty Gracza ****', 'red'))
        print(table)
        print(" ")
        stop = input('naciśnij enter aby powrócić: ')
        clear_terminal()

    def czy_gracz_umarl(self):
        # sprawdzanie czy gracz umarł
        return self.hp <= 0
