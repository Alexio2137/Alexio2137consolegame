#Aleks

from podroze.podroz_do_krainy import PodrozDoKrainy
from walka import Walka
from rich.console import Console
from rich.table import Table
from gracz import Gracz
from dane import DaneGry
from Akcje import Akcje
from dane import clear_terminal

console = Console()

dane_gry = DaneGry()
# Wywołanie metody lokalizacje, która utworzy atrybut krainy
dane_gry.lokalizacje()


class Podroz:

    @staticmethod
    def menu_podrozy(gracz):  # Added gracz parameter
        while True:
            console.clear()
            table = Table(title="=== Menu Podróży ===", show_header=False, header_style="bold magenta")
            table.add_column('Atrybut', style="cyan")
            table.add_column('Wartość', style="cyan")

            table.add_row('Punkty życia (HP)', f"[red]{gracz.hp}[/red]")
            table.add_row('Poziom wytrzymałości', f"[green]{gracz.stamina}[/green]")
            table.add_row('Poziom energii', f"[red]{gracz.energia}[/red]")
            table.add_row('Poziom głodu', f"[red]{gracz.effekty['glod']}[/red]")
            table.add_row('Poziom napojenia', f"[red]{gracz.effekty['pragnienie']}[/red]")

            options_table = Table(show_header=False, header_style="bold cyan")
            options_table.add_column('#', style="yellow")
            options_table.add_column('Opcja', style="yellow")
            options_table.add_row('1', 'Pokaż menu Gracza')
            options_table.add_row('2', 'Przejdź do menu akcji')
            options_table.add_row('3', 'Podróżuj do krainy ...')
            options_table.add_row('4', 'Użyj mapy')
            options_table.add_row('5', 'Losowa podróż')
            options_table.add_row('6', 'Powrót')

            console.print(table)
            console.print(options_table)

            wybor_opcji_podrozy = input('Podaj swój wybór: ')

            if wybor_opcji_podrozy == '1':
                console.clear()
                Gracz.menu_gracza(gracz)
            elif wybor_opcji_podrozy == '2':
                console.clear()
                Akcje.menu_akcji(gracz)
            elif wybor_opcji_podrozy == '3':
                console.clear()
                PodrozDoKrainy().menu_wyboru_krainy(dane_gry, gracz)  # Added call to PodrozDoKrainy().menu_wyboru_krainy
            elif wybor_opcji_podrozy == '4':
                console.clear()
                # Tutaj dodaj logikę dla opcji 4 - Użyj mapy
                pass
            elif wybor_opcji_podrozy == '5':
                console.clear()
                # Tutaj dodaj logikę dla opcji 5 - Losowa podróż
                pass
            elif wybor_opcji_podrozy == '6':
                console.clear()
                break
            else:
                console.print("[red]Nieprawidłowy wybór. Spróbuj ponownie.[/red]")
