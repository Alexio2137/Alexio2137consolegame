
from rich.console import Console
from rich.table import Table
from dane import DaneGry
from dane import clear_terminal
from gracz import Gracz
from mechaniki import odpocznij, zjedz, napij_sie

console = Console()

class Akcje:
    def menu_akcji(self):
        while True:
            console.clear()
            table = Table(title="[blue]Menu Akcji[/blue]", show_header=False, header_style="bold blue")
            table.add_column('[cyan]#[/cyan]')
            table.add_column('[cyan]Akcja[/cyan]')

            table.add_row('[yellow]1[/yellow]', '[green]Odpocznij[/green]')
            table.add_row('[yellow]2[/yellow]', '[yellow]Zjedz[/yellow]')
            table.add_row('[yellow]3[/yellow]', '[cyan]Napij się[/cyan]')
            table.add_row('[yellow]4[/yellow]', '[red]Powrót[/red]')

            console.print(table)

            wybor = input("Wybierz numer akcji (1-4): ")

            if wybor == '1':
                console.clear()
                odpocznij()
            elif wybor == '2':
                console.clear()
                zjedz()
            elif wybor == '3':
                console.clear()
                napij_sie()
            elif wybor == '4':
                break
            else:
                console.print("[red]Nieprawidłowy wybór. Spróbuj ponownie.[/red]")