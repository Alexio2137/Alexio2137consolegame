#Aleks, Wojtek i Mateusz

from rich.console import Console
from rich.table import Table
from rich import print as rprint
from dane import clear_terminal
from dane import DaneGry
console = Console()




class Gracz:
    def __init__(self, imie, poziom_trudnosci):
        self.imie = imie
        self.hp = 100
        self.ap = 50
        self.bonus_ap = 0
        self.dp = 30
        self.bonus_dp = 0
        self.stamina = 100
        self.energia = 100
        self.coiny = 0
        self.effekty = {
            'glod': 50,
            'maxglod': 100,
            'pragnienie': 30,
            'maxpragnienie': 60,
            'zatrucie_potka': 0,
            'max_zatrucie_potka': 50,
        }
        self.poziom_trudnosci = poziom_trudnosci
        self.statystyki = {
            'Zabujstwa': 0,
            'podroze': 0,
            'zdobyte_zloto': 0,
            'zlowione_ryby': 0,
            'sprzedane_itemy': 0,
            'uzyte_potki': 0
        }
        self.mapa = {
            'miasta': [],
            'wsie': [],
            'osady': [],
            'obozy': []
        }
        self.skile = {
            'dodatkowe_ataki': [],
            'dodatkowe_obrony': [],
            'zaklecia': []
        }
        self.poziomy = {
            'lvl': 1,
            'xp': 0,
            'tradelvl': 1,
            'tradexp': 0,
            'fishlvl': 1,
            'fishxp': 0,
            'battlelvl': 1,
            'battlexp': 0
        }
        self.wyposazenie = {
            'helm': None,
            'zbroja': None,
            'buty': None,
            'rekawice': None,
            'bron': None,
            'tarcza': None,
            'bron_dodatkowa': None,
            'kon': None,
            'tools': None
        }
        self.eq_informacje = {
            'sloty': 0,
            'maxsloty': 20,
            'bonussloty': 0,
            'obciarzenie': 0,
            'maxobciazenie': 20,
            'bonusobciazenia': 0
        }
        self.inventory = {
            'rzeczy': {
                'hełmy': [{'nazwa': '', 'ilosc': 0}],
                'zbroje': [{'nazwa': '', 'ilosc': 0}],
                'buty': [{'nazwa': '', 'ilosc': 0}],
                'rękawice': [{'nazwa': '', 'ilosc': 0}],
                'bronie': [{'nazwa': '', 'ilosc': 0}],
                'narzędzia': [{'nazwa': '', 'ilosc': 0}],
                'potki': {
                    'leczące': [{'nazwa': '', 'ilosc': 0}],
                    'zwiększające ap': [{'nazwa': '', 'ilosc': 0}],
                    'zwiększające dp': [{'nazwa': '', 'ilosc': 0}],
                    'odnawiające energie': [{'nazwa': '', 'ilosc': 0}]
                }
            },
            'picia': [{'nazwa': '', 'ilosc': 0}],
            'jedzenie': [{'nazwa': '', 'ilosc': 0}],
            'looty': [{'nazwa': '', 'ilosc': 0}],
            'stajnia': [{'nazwa': '', 'ilosc': 0}],
            'inne': [{'nazwa': '', 'ilosc': 0}]
        }

    def odejmij_stamine(self, ilosc_staminy):
        if ilosc_staminy > 0:
            poziomy_trudnosci = {
                'Normalny': 1.0,
                'Trudny': 1.2,
                'Ekstremalny': 1.5,
                'Niemożliwy': 2.0,
            }

            mnoznik_staminy = poziomy_trudnosci.get(self.poziom_trudnosci, 1.0)

            ilosc_staminy *= mnoznik_staminy

            if self.stamina >= ilosc_staminy:
                self.stamina -= ilosc_staminy
            else:
                print(f"{self.imie} nie ma wystarczającej ilości staminy.")
        else:
            print("Ilość staminy do odjęcia musi być większa niż 0.")
    def odejmij_glod(self, ilosc_glodu):
        if ilosc_glodu > 0:
            poziomy_trudnosci = {
                'Normalny': 1.0,
                'Trudny': 1.2,
                'Ekstremalny': 1.5,
                'Niemożliwy': 2.0,
            }
    

            mnoznik_glodu = poziomy_trudnosci.get(self.poziom_trudnosci, 1.0)

            ilosc_glodu *= mnoznik_glodu

            if self.effekty['glod'] >= ilosc_glodu:
                self.effekty['glod'] -= ilosc_glodu
            else:
                print(f"{self.imie} nie ma wystarczającej ilości jedzenia.")
                # Tutaj możesz dodać kod do odjęcia życia w zależności od poziomu trudności
                odjecie_zycia = 0  # Domyślne odjęcie życia
                if self.poziom_trudnosci == 'Trudny':
                    odjecie_zycia = 10
                elif self.poziom_trudnosci == 'Ekstremalny':
                    odjecie_zycia = 20
                elif self.poziom_trudnosci == 'Niemożliwy':
                    odjecie_zycia = 30

                # Odjęcie życia
                self.hp -= odjecie_zycia
                print(f"{self.imie} traci {odjecie_zycia} życia!")

        else:
            print("Ilość jedzenia do odjęcia musi być większa niż 0.")
    def odejmij_picie(self, ilosc_picia):
        if ilosc_picia > 0:
            poziomy_trudnosci = {
                'Normalny': 1.0,
                'Trudny': 1.2,
                'Ekstremalny': 1.5,
                'Niemożliwy': 2.0,
            }

            mnoznik_picia = poziomy_trudnosci.get(self.poziom_trudnosci, 1.0)

            ilosc_picia *= mnoznik_picia

            if self.effekty['pragnienie'] >= ilosc_picia:
                self.effekty['pragnienie'] -= ilosc_picia
            else:
                print(f"{self.imie} nie ma wystarczającej ilości do picia.")
                # Tutaj możesz dodać kod do odjęcia zdrowia w zależności od poziomu trudności
                odjecie_zdrowia = 5  # Domyślne odjęcie zdrowia
                if self.poziom_trudnosci == 'Trudny':
                    odjecie_zdrowia += 10
                elif self.poziom_trudnosci == 'Ekstremalny':
                    odjecie_zdrowia += 20
                elif self.poziom_trudnosci == 'Niemożliwy':
                    odjecie_zdrowia += 30

                # Odjęcie zdrowia
                self.hp -= odjecie_zdrowia
                print(f"{self.imie} traci {odjecie_zdrowia} zdrowia!")

        else:
            print("Ilość płynu do odjęcia musi być większa niż 0.")
    def odejmij_energie(self, ilosc_energii):
        if ilosc_energii > 0:
            poziomy_trudnosci = {
                'Normalny': 1.0,
                'Trudny': 1.2,
                'Ekstremalny': 1.5,
                'Niemożliwy': 2.0,
            }

            mnoznik_energii = poziomy_trudnosci.get(self.poziom_trudnosci, 1.0)

            ilosc_energii *= mnoznik_energii

            if self.energia >= ilosc_energii:
                self.energia -= ilosc_energii
            else:
                print(f"{self.imie} nie ma wystarczającej ilości energii.")
                # Tutaj możesz dodać kod do odjęcia zdrowia w zależności od poziomu trudności
                odjecie_zdrowia = 5  # Domyślne odjęcie zdrowia
                if self.poziom_trudnosci == 'Trudny':
                    odjecie_zdrowia += 10
                elif self.poziom_trudnosci == 'Ekstremalny':
                    odjecie_zdrowia += 20
                elif self.poziom_trudnosci == 'Niemożliwy':
                    odjecie_zdrowia += 30

                # Odjęcie zdrowia
                self.hp -= odjecie_zdrowia
                print(f"{self.imie} traci {odjecie_zdrowia} zdrowia!")

        else:
            print("Ilość energii do odjęcia musi być większa niż 0.")

    def zwieksz_poziom(self, dodatkowe_xp):
        poziomy_trudnosci = {
                'Normalny': {'mnoznik_ap': 2.5, 'mnoznik_hp': 2.0, 'mnoznik_dp': 2.0, 'mnoznik_xp': 1.2},
                'Trudny': {'mnoznik_ap': 2.0, 'mnoznik_hp': 1.5, 'mnoznik_dp': 1.5, 'mnoznik_xp': 1.5},
                'Ekstremalny': {'mnoznik_ap': 1.5, 'mnoznik_hp': 1.2, 'mnoznik_dp': 1.2, 'mnoznik_xp': 2.0},
                'Niemożliwy': {'mnoznik_ap': 1.2, 'mnoznik_hp': 1.0, 'mnoznik_dp': 1.0, 'mnoznik_xp': 2.5},
            }

        mnozniki = poziomy_trudnosci.get(self.poziom_trudnosci, {'mnoznik_ap': 1.0, 'mnoznik_hp': 1.0, 'mnoznik_dp': 1.0, 'mnoznik_xp': 1.0})
        mnoznik_ap = mnozniki['mnoznik_ap']
        mnoznik_hp = mnozniki['mnoznik_hp']
        mnoznik_dp = mnozniki['mnoznik_dp']
        mnoznik_xp = mnozniki['mnoznik_xp']

        wymagane_xp = self.poziomy['lvl'] * mnoznik_xp + 100

        if dodatkowe_xp >= wymagane_xp:
            self.poziomy['lvl'] += 1
            self.poziomy['xp'] = dodatkowe_xp - wymagane_xp

            # Zwiększanie HP, AP i DP zależne od poziomu trudności
            zdobywane_hp = int(5 * mnoznik_hp)  # Przykładowe zwiększenie HP zależne od poziomu trudności
            zdobywane_ap = int(1 * mnoznik_ap)    # Przykładowe zwiększenie AP zależne od poziomu trudności
            zdobywane_dp = int(1 * mnoznik_dp)    # Przykładowe zwiększenie DP zależne od poziomu trudności

            self.hp += zdobywane_hp
            self.ap += zdobywane_ap
            self.dp += zdobywane_dp

            print(f"{self.imie} awansował na poziom {self.poziomy['lvl']}!")
            print(f"{self.imie} zdobył {zdobywane_hp} HP, {zdobywane_ap} AP, {zdobywane_dp} DP.")
        else:
            self.poziomy['xp'] += dodatkowe_xp
    
    def zdobadz_battle_xp(self, dodatkowe_xp):
        poziomy_trudnosci = {
            'Normalny': {'mnoznik_ap': 2.5, 'mnoznik_hp': 2.0, 'mnoznik_dp': 2.0, 'mnoznik_xp': 1.2},
            'Trudny': {'mnoznik_ap': 2.0, 'mnoznik_hp': 1.5, 'mnoznik_dp': 1.5, 'mnoznik_xp': 1.5},
            'Ekstremalny': {'mnoznik_ap': 1.5, 'mnoznik_hp': 1.2, 'mnoznik_dp': 1.2, 'mnoznik_xp': 2.0},
            'Niemożliwy': {'mnoznik_ap': 1.2, 'mnoznik_hp': 1.0, 'mnoznik_dp': 1.0, 'mnoznik_xp': 2.5},
        }

        # Funkcja do obsługi zdobywania battle xp
        self.poziomy['battlexp'] += dodatkowe_xp * poziomy_trudnosci['mnoznik_xp']
        print(f"{self.imie} zdobył {dodatkowe_xp * poziomy_trudnosci['mnoznik_xp']:.2f} XP w walce.")

        # Sprawdź, czy zdobyto wystarczająco dużo xp do awansu
        wymagane_xp = self.poziomy['battlelvl'] * poziomy_trudnosci['mnoznik_xp'] * 100

        if self.poziomy['battlexp'] >= wymagane_xp:
            # Aktualizuj poziom, resetuj xp do nowego poziomu
            self.poziomy['battlelvl'] += 1
            self.poziomy['battlexp'] = 0  # Zresetuj battle xp

            # Aktualizuj poziomy statystyk (HP, AP, DP) zależne od poziomu trudności
            zdobywane_hp = int(3 * poziomy_trudnosci['mnoznik_hp'])
            zdobywane_ap = int(2 * poziomy_trudnosci['mnoznik_ap'])
            zdobywane_dp = int(2 * poziomy_trudnosci['mnoznik_dp'])
            self.hp += zdobywane_hp
            self.ap += zdobywane_ap
            self.dp += zdobywane_dp

            print(f"{self.imie} awansował na poziom w walce: {self.poziomy['battlelvl']}!")
            print(f"{self.imie} zdobył {zdobywane_hp} HP, {zdobywane_ap} AP, {zdobywane_dp} DP.")
        else:
            print(f"{self.imie} zdobył {self.poziomy['battlexp']:.2f} XP w walce, ale to nie wystarczyło do awansu na kolejny poziom.")
    
    def zdobadz_fishing_xp(self, dodatkowe_xp):
        poziomy_trudnosci = {
            'Normalny': {'mnoznik_ap': 2.5, 'mnoznik_hp': 2.0, 'mnoznik_dp': 2.0, 'mnoznik_xp': 1.2},
            'Trudny': {'mnoznik_ap': 2.0, 'mnoznik_hp': 1.5, 'mnoznik_dp': 1.5, 'mnoznik_xp': 1.5},
            'Ekstremalny': {'mnoznik_ap': 1.5, 'mnoznik_hp': 1.2, 'mnoznik_dp': 1.2, 'mnoznik_xp': 2.0},
            'Niemożliwy': {'mnoznik_ap': 1.2, 'mnoznik_hp': 1.0, 'mnoznik_dp': 1.0, 'mnoznik_xp': 2.5},
        }

        # Funkcja do obsługi zdobywania fishing xp
        self.poziomy['fishxp'] += dodatkowe_xp * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_xp']
        print(f"{self.imie} zdobył {dodatkowe_xp * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_xp']:.2f} XP w łowieniu ryb.")

        # Sprawdź, czy zdobyto wystarczająco dużo xp do awansu
        wymagane_xp = self.poziomy['fishlvl'] * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_xp'] * 100

        if self.poziomy['fishxp'] >= wymagane_xp:
            # Aktualizuj poziom, resetuj xp do nowego poziomu
            self.poziomy['fishlvl'] += 1
            self.poziomy['fishxp'] = 0  # Zresetuj fishing xp

            # Aktualizuj poziomy statystyk (HP) zależne od poziomu trudności
            zdobywane_hp = int(3 * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_hp'])
            self.hp += zdobywane_hp

            print(f"{self.imie} awansował na poziom w łowieniu ryb: {self.poziomy['fishlvl']}!")
            print(f"{self.imie} zdobył {zdobywane_hp} HP.")
        else:
            print(f"{self.imie} zdobył {self.poziomy['fishxp']:.2f} XP w łowieniu ryb, ale to nie wystarczyło do awansu na kolejny poziom.")

    def zdobadz_trade_xp(self, dodatkowe_xp):
        poziomy_trudnosci = {
            'Normalny': {'mnoznik_ap': 2.5, 'mnoznik_hp': 2.0, 'mnoznik_dp': 2.0, 'mnoznik_xp': 1.2},
            'Trudny': {'mnoznik_ap': 2.0, 'mnoznik_hp': 1.5, 'mnoznik_dp': 1.5, 'mnoznik_xp': 1.5},
            'Ekstremalny': {'mnoznik_ap': 1.5, 'mnoznik_hp': 1.2, 'mnoznik_dp': 1.2, 'mnoznik_xp': 2.0},
            'Niemożliwy': {'mnoznik_ap': 1.2, 'mnoznik_hp': 1.0, 'mnoznik_dp': 1.0, 'mnoznik_xp': 2.5},
        }

        # Funkcja do obsługi zdobywania trade xp
        self.poziomy['tradexp'] += dodatkowe_xp * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_xp']
        print(f"{self.imie} zdobył {dodatkowe_xp * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_xp']:.2f} XP w handlu.")

        # Sprawdź, czy zdobyto wystarczająco dużo xp do awansu
        wymagane_xp = self.poziomy['tradelvl'] * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_xp'] * 100

        if self.poziomy['tradexp'] >= wymagane_xp:
            # Aktualizuj poziom, resetuj xp do nowego poziomu
            self.poziomy['tradelvl'] += 1
            self.poziomy['tradexp'] = 0  # Zresetuj trade xp

            # Aktualizuj poziomy statystyk (HP) zależne od poziomu trudności
            zdobywane_hp = int(3 * poziomy_trudnosci[self.poziom_trudnosci]['mnoznik_hp'])
            self.hp += zdobywane_hp

            print(f"{self.imie} awansował na poziom w handlu: {self.poziomy['tradelvl']}!")
            print(f"{self.imie} zdobył {zdobywane_hp} HP.")
        else:
            print(f"{self.imie} zdobył {self.poziomy['tradexp']:.2f} XP w handlu, ale to nie wystarczyło do awansu na kolejny poziom.")

    def dodaj_bonus_ap(self, bonus):
        self.bonus_ap += bonus
        self.ap += bonus

    def odejmij_bonus_ap(self, bonus):
        self.bonus_ap -= bonus
        self.ap -= bonus

    def dodaj_bonus_dp(self, bonus):
        self.bonus_dp += bonus
        self.dp += bonus

    def odejmij_bonus_dp(self, bonus):
        self.bonus_dp -= bonus
        self.dp -= bonus

    def menu_gracza(self):
        while True:
            console.clear()
            table = Table(title="[bold cyan]Menu Gracza[/bold cyan]")

            table.add_column("[cyan]# [/cyan]")
            table.add_column("[cyan]Opcja[/cyan]")

            table.add_row("1", "[green]Informacje o graczu[/green]")
            table.add_row("2", "[yellow]Skile[/yellow]")
            table.add_row("3", "[cyan]Poziomy[/cyan]")
            table.add_row("4", "[blue]Inventory informacje[/blue]")
            table.add_row("5", "[red]Effekty[/red]")
            table.add_row("6", "[red]Powrót[/red]")

            console.print(table)
            menu_gracza_wybor = input('Wybierz opcję: ')

            if menu_gracza_wybor == '1':
                console.clear()
                self.informacje_o_graczu()
            elif menu_gracza_wybor == '2':
                console.clear()
                self.skile_gracza()
            elif menu_gracza_wybor == '3':
                console.clear()
                self.poziomy_gracza()
            elif menu_gracza_wybor == '4':
                console.clear()
                self.inventory_informacje()
            elif menu_gracza_wybor == '5':
                console.clear()
                self.wyswietl_effekty()
            elif menu_gracza_wybor == '6':
                console.clear()
                break
            else:
                console.print('[red]Nieprawidłowy wybór. Spróbuj ponownie.[/red]')

    def informacje_o_graczu(self):
        table = Table(title="[bold green]Informacje o Graczu[/bold green]")

        table.add_column("[cyan]Atrybut[/cyan]", "[cyan]Wartość[/cyan]")
        table.add_row("Imię", f"[cyan]{self.imie}[/cyan]")
        table.add_row("Poziom Trudności", f"[green]{self.poziom_trudnosci}[/green]")
        table.add_row("Punkty życia (HP)", f"[red]{self.hp}[/red]")
        table.add_row("Punkty ataku (AP)", f"[yellow]{self.ap + self.bonus_ap}[/yellow]")
        table.add_row("Punkty obrony (DP)", f"[yellow]{self.dp + self.bonus_dp}[/yellow]")
        table.add_row("Poziom wytrzymałości", f"[green]{self.stamina}[/green]")
        table.add_row("Poziom energii", f"[green]{self.energia}[/green]")
        table.add_row("Ilość monet", f"[yellow]{self.coiny}[/yellow]")

        console.print(table)
        console.input('[blue]Naciśnij enter aby powrócić: [/blue]')
        console.clear()

    def skile_gracza(self):
        table = Table(title="[bold yellow]Umiejętności Gracza[/bold yellow]")

        table.add_column("[yellow]Rodzaj umiejętności[/yellow]", "[yellow]Lista umiejętności[/yellow]")
        table.add_row("Dodatkowe ataki", f"[yellow]{', '.join(self.skile['dodatkowe_ataki'])}[/yellow]")
        table.add_row("Dodatkowe obrony", f"[yellow]{', '.join(self.skile['dodatkowe_obrony'])}[/yellow]")
        table.add_row("Zaklęcia", f"[yellow]{', '.join(self.skile['zaklecia'])}[/yellow]")

        console.print(table)
        console.input('[blue]Naciśnij enter aby powrócić: [/blue]')
        console.clear()

    def poziomy_gracza(self):
        table = Table(title=" Poziomy Gracza ", title_style="cyan")
        table.add_column("Typ poziomu", style="cyan")
        table.add_column("Poziom", style="cyan")
        table.add_column("Punkty doświadczenia", style="cyan")

        table.add_row("Doświadczenie ogólne (lvl)", str(self.poziomy['lvl']), str(self.poziomy['xp']))
        table.add_row("Handel", str(self.poziomy['tradelvl']), str(self.poziomy['tradexp']))
        table.add_row("Łowienie", str(self.poziomy['fishlvl']), str(self.poziomy['fishxp']))
        table.add_row("Walka", str(self.poziomy['battlelvl']), str(self.poziomy['battlexp']))

        console.print(table)
        console.input("Naciśnij enter aby powrócić: ")
        console.clear()

    def inventory_informacje(self):
        table = Table(title="[bold blue]Informacje o Ekwipunku[/bold blue]")

        table.add_column("[blue]Informacje o Ekwipunku[/blue]", "[blue]Wartość[/blue]")
        table.add_row("Liczba slotów", f"[blue]{self.eq_informacje['sloty']} / {self.eq_informacje['maxsloty']}[/blue]")
        table.add_row("Bonus slotów", f"[blue]{self.eq_informacje['bonussloty']}[/blue]")
        table.add_row("Obciążenie", f"[blue]{self.eq_informacje['obciarzenie']} / {self.eq_informacje['maxobciazenie']}[/blue]")
        table.add_row("Bonus obciążenia", f"[blue]{self.eq_informacje['bonusobciazenie']}[/blue]")

        console.print(table)
        console.input('[blue]Naciśnij enter aby powrócić: [/blue]')
        console.clear()

    def wyswietl_effekty(self):
        table = Table(title="[bold red]Efekty Gracza[/bold red]")

        table.add_column("[red]Efekt[/red]", "[red]Wartość[/red]")
        for efekt, wartosc in self.effekty.items():
            table.add_row(efekt.capitalize(), f"[red]{wartosc}[/red]")

        console.print(table)
        console.input('[blue]Naciśnij enter aby powrócić: [/blue]')
        console.clear()

    def czy_gracz_umarl(self):
        return self.hp <= 0