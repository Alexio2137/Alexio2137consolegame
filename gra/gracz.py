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
            'bonusobciazenie': 0
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

    def menu_gracza(self):
        while True:
            console.clear()
            table = Table(title="[bold cyan]Menu Gracza[/bold cyan]")

            table.add_column("[cyan]# [/cyan]")
            table.add_column("[cyan]Opcja[/cyan]")

            table.add_row("1", "[green]Informacje o graczu[/green]")
            table.add_row("2", "[yellow]Skile[/yellow]")
            table.add_row("3", "[cyan]Poziomy[/cyan]")
            table.add_row("4", "[magenta]Wyposażenie[/magenta]")
            table.add_row("5", "[blue]Inventory informacje[/blue]")
            table.add_row("6", "[red]Effekty[/red]")
            table.add_row("7", "[red]Powrót[/red]")

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
                self.wyposazenie_gracza()
            elif menu_gracza_wybor == '5':
                console.clear()
                self.inventory_informacje()
            elif menu_gracza_wybor == '6':
                console.clear()
                self.wyswietl_effekty()
            elif menu_gracza_wybor == '7':
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

    def wyposazenie_gracza(self):
        table = Table(title="[bold magenta]Wyposażenie Gracza[/bold magenta]")

        table.add_column("[magenta]Slot wyposażenia[/magenta]", "[magenta]Przedmiot[/magenta]")
        for slot, przedmiot in self.wyposazenie.items():
            table.add_row(slot.capitalize(), f"[magenta]{przedmiot if przedmiot else '-'}[/magenta]")

        console.print(table)
        console.input('[blue]Naciśnij enter aby powrócić: [/blue]')
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