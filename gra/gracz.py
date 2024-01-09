#Aleks, Wojtek i Mateusz

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
        self.inventory = {
            
        }

    def menu_gracza(self):
        while True:
            print(colored('**** Menu Gracza ****', 'blue'))
            print('1. Informacje o graczu')
            print('2. Skile')
            print('3. Poziomy')
            print('4. Wyposażenie')
            print('5. Inventory')
            print('6. Powrót')

            menu_gracza_wybor = input('Wybierz opcję: ')

            if menu_gracza_wybor == '1':
                self.informacje_o_graczu()
            elif menu_gracza_wybor == '2':
                self.skile_gracza()
            elif menu_gracza_wybor == '3':
                self.poziomy_gracza()
            elif menu_gracza_wybor == '4':
                self.wyposazenie_gracza()
            elif menu_gracza_wybor == '5':
                self.inventory_gracza()
            elif menu_gracza_wybor == '6':
                break
            else:
                print(colored('Nieprawidłowy wybór. Spróbuj ponownie.', 'red'))

    def informacje_o_graczu(self):
        table = PrettyTable(['Atrybut', 'Wartość'])
        table.add_row(['Imię', self.imie])
        table.add_row(['Punkty życia (HP)', str(self.hp)])
        table.add_row(['Punkty ataku (AP)', str(self.ap + self.bonus_ap)])
        table.add_row(['Punkty obrony (DP)', str(self.dp + self.bonus_dp)])
        table.add_row(['Poziom wytrzymałości', str(self.stamina)])
        table.add_row(['Poziom energii', str(self.energia)])
        table.add_row(['Ilość monet', str(self.coiny)])

        print(colored('**** Informacje o Graczu ****', 'green'))
        print(table)

    def skile_gracza(self):
        table = PrettyTable(['Rodzaj umiejętności', 'Lista umiejętności'])
        table.add_row(['Dodatkowe ataki', ', '.join(self.skile['dodatkowe_ataki'])])
        table.add_row(['Dodatkowe obrony', ', '.join(self.skile['dodatkowe_obrony'])])
        table.add_row(['Zaklęcia', ', '.join(self.skile['zaklecia'])])

        print(colored('**** Umiejętności Gracza ****', 'yellow'))
        print(table)

    def poziomy_gracza(self):
        table = PrettyTable(['Typ poziomu', 'Poziom', 'Punkty doświadczenia'])
        table.add_row(['Doświadczenie ogólne (lvl)', str(self.poziomy['lvl']), str(self.poziomy['xp'])])
        table.add_row(['Handel', str(self.poziomy['tradelvl']), str(self.poziomy['tradexp'])])
        table.add_row(['Łowienie', str(self.poziomy['fishlvl']), str(self.poziomy['fishxp'])])
        table.add_row(['Walka', str(self.poziomy['battlelvl']), str(self.poziomy['battlexp'])])

        print(colored('**** Poziomy Gracza ****', 'blue'))
        print(table)

    def wyposazenie_gracza(self):
        table = PrettyTable(['Slot wyposażenia', 'Przedmiot'])
        for slot, przedmiot in self.wyposazenie.items():
            table.add_row([slot.capitalize(), przedmiot if przedmiot else '-'])

        print(colored('**** Wyposażenie Gracza ****', 'magenta'))
        print(table)

    def czy_gracz_umarl(self):
        # sprawdzanie czy gracz umarł
        return self.hp <= 0