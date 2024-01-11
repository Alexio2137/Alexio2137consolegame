from rich.console import Console # pip install rich
from rich.table import Table
from rich import print
from dane import DaneGry
from dane import clear_terminal
from gracz import Gracz
from osada import Osada
from inventory import Inventory
from fishing import Fishing
from podroz import Podroz
from Akcje import Akcje
from enchanty import Enchanty

console = Console()

def stworz_nowego_gracza(dane_gry):
    while True:
        imie = input("Podaj imię gracza: ")
        if imie.strip():
            break
        else:
            print("[bold red]Imię nie może być puste. Spróbuj ponownie.[/bold red]")

    nowy_gracz = Gracz(imie)
    return nowy_gracz

nowy_gracz = stworz_nowego_gracza(DaneGry())  


while nowy_gracz.hp > 0:
    clear_terminal()
    table = Table(show_lines=True)
    
    # Znalezienie najdłuższego wiersza w menu głównym
    max_row_length = max(len("[yellow]1[/yellow]"), len("[yellow]2[/yellow]"), len("[yellow]3[/yellow]"), len("[yellow]4[/yellow]"))

    # Ustawienie szerokości tabeli na długość najdłuższego wiersza
    table.column_widths = [max_row_length]

    # Dodawanie kolumn do tabeli
    table.add_column("[cyan]# [/cyan]", justify="center", style="bold cyan")
    table.add_column("[cyan]=== Główne Menu === [/cyan]", style="bold cyan")

    # Dodawanie danych do tabeli
    table.add_row("[yellow]1[/yellow]", "[green]Gracz[/green]")
    table.add_row("[yellow]2[/yellow]", "[yellow]Podróże[/yellow]")
    table.add_row("[yellow]3[/yellow]", "[cyan]Akcje[/cyan]")
    table.add_row("[yellow]4[/yellow]", "[red]Wyjście[/red]")

    # Wyświetlanie tabeli
    console.print(table)

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nowy_gracz.menu_gracza()
    elif wybor == "2":
        Podroz.menu_podrozy(nowy_gracz)  
    elif wybor == "3":
        Akcje.menu_akcji(nowy_gracz)  
    elif wybor == "4":
        console.print("[bold red]Dziękujemy za grę. Do zobaczenia![/bold red]")
        break
    else:
        console.print("[bold yellow]Niepoprawny wybór. Spróbuj ponownie.[/bold yellow]")
