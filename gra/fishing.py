#Mateusz
import random as r
import time
from rich.progress import Progress
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from dane import clear_terminal
from dane import DaneGry
from gracz import Gracz

console = Console()

dane_gry = DaneGry()



def fishing_process():
    fishing_time = r.randrange(2, 15)
    loading_time = fishing_time * 5
    
    with Progress(transient=True) as progress:
        task = progress.add_task("[cyan]Trwa wędkowanie...", total=loading_time)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.2)
            
    rprint("[yellow]Złowiłeś rybę![/yellow]")

def fishing():
    while True:
        fishing_rozpocznij = input(console.print("[cyan]F aby zarzucić wędkę[/cyan]", style="cyan"))
        if fishing_rozpocznij.lower() == 'f':
            fishing_process()
        else:
            break

class Fishing:
    @staticmethod
    def menu_fishing():
        while True:
            table = Table(show_lines=True)

            # Dodawanie kolumn do tabeli
            table.add_column("[cyan]# [/cyan]", justify="center", style="bold cyan")
            table.add_column("[cyan]Opcja[/cyan]", style="bold cyan")

            # Dodawanie danych do tabeli
            table.add_row("[yellow]1[/yellow]", "[green]Zacznij łowić[/green]")
            table.add_row("[yellow]2[/yellow]", "[yellow]Wyświetl ryby w ekwipunku[/yellow]")
            table.add_row("[yellow]3[/yellow]", "[red]Wyjście[/red]")

            # Ustawianie koloru nagłówka
            table.title = "[bold blue]=== Menu wędkowania ===[/bold blue]"

            # Wyświetlanie tabeli
            console.print(table)

            wybor_fishing = input("Wybierz opcję: ")

            if wybor_fishing == "1":
                fishing()
            elif wybor_fishing == "2":
                pass  # Tutaj dodaj kod dla opcji 2
            elif wybor_fishing == "3":
                clear_terminal()
                break
            else:
                console.print("[bold red]Niepoprawny wybór. Spróbuj ponownie.[/bold red]")



'''
 def dodaj_rybe_do_inventory(self, nazwa_ryby, ilosc=1):
        if nazwa_ryby in dane_gry.ryby:
            if 'ryby' not in self.inventory:
                self.inventory['ryby'] = {nazwa_ryby: ilosc}
            else:
                if nazwa_ryby in self.inventory['ryby']:
                    self.inventory['ryby'][nazwa_ryby] += ilosc
                else:
                    self.inventory['ryby'][nazwa_ryby] = ilosc
        else:
            print(f"Ryba {nazwa_ryby} nie istnieje w danych gry.")

 def fishing_process(self):
        fishing_time = r.randrange(2, 15)
        loading_time = fishing_time * 5

        with Progress(transient=True) as progress:
            task = progress.add_task("[cyan]Trwa wędkowanie...", total=loading_time)
            while not progress.finished:
                progress.update(task, advance=1)
                time.sleep(0.2)

        rprint("[yellow]Złowiłeś rybę![/yellow]")

        # Dodawanie złowionej ryby do inventory gracza
        nazwa_ryby = r.choice(list(dane_gry.ryby.keys()))
        ilosc_ryb = r.randint(1, 3)  # Możesz dostosować ilość złowionych ryb
        self.gracz.dodaj_rybe_do_inventory(nazwa_ryby, ilosc_ryb)           
'''