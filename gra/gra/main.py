from rich.console import Console # pip install rich
from rich.table import Table
from rich.panel import Panel
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
from mechaniki import informacje_o_grze, autorzy

console = Console()

def wybierz_poziom_trudnosci():
    clear_terminal()
    table = Table(title="Wybierz poziom trudności", title_style="bold magenta")
    table.add_column("Numer", style="cyan", justify="center")
    table.add_column("Poziom trudności", style="bold green", justify="center")

    table.add_row("1", "Normalny")
    table.add_row("2", "Trudny")
    table.add_row("3", "Ekstremalny")
    table.add_row("4", "Niemożliwy")

    console.print(table)
    
    while True:
        wybor_poziomu = input("Twój wybór: ")

        if wybor_poziomu in ["1", "2", "3", "4"]:
            return {
                "1": "Normalny",
                "2": "Trudny",
                "3": "Ekstremalny",
                "4": "Niemożliwy"
            }[wybor_poziomu]
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
def game_start():
    console.print("[bold cyan]Mroczne Przejścia:[/bold cyan]")
    console.print("[italic]Eksplozja Handlu i Wojenne Wyprawy[/italic]")
    console.print()

    while True:
        clear_terminal()
        start_menu_table = Table(show_lines=True)
        start_menu_table.add_column("[cyan]# [/cyan]", justify="center", style="bold cyan")
        start_menu_table.add_column("[cyan]=== Menu Startowe ===[/cyan]", style="bold cyan")
        start_menu_table.add_row("[yellow]1[/yellow]", "[green]Rozpocznij Grę[/green]")
        start_menu_table.add_row("[yellow]2[/yellow]", "[magenta]Informacje o Grze[/magenta]")
        start_menu_table.add_row("[yellow]3[/yellow]", "[blue]Autorzy[/blue]")

        console.print(start_menu_table)

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            clear_terminal()
            # Rozpocznij Grę
            start_game_table = Table(show_lines=True)
            start_game_table.add_column("[cyan]# [/cyan]", justify="center", style="bold cyan")
            start_game_table.add_column("[cyan]=== Menu Startowe ===[/cyan]", style="bold cyan")
            start_game_table.add_row("[yellow]1[/yellow]", "[green]Stwórz postać[/green]")
            start_game_table.add_row("[yellow]2[/yellow]", "[magenta]Wczytaj grę[/magenta]")
            start_game_table.add_row("[yellow]3[/yellow]", "[blue]Zagraj jako gość[/blue]")
            console.print(start_game_table)

            wybor_start_game = input("Wybierz opcję: ")

            if wybor_start_game == "1":
                clear_terminal()
                gracz_imie = input("Podaj imię gracza: ")
                poziom_trudnosci = wybierz_poziom_trudnosci()
                gracz = Gracz(gracz_imie, poziom_trudnosci)

                return gracz
            elif wybor_start_game == "2":
                clear_terminal()
                console.print("[bold red]Funkcja Wczytaj Grę jest obecnie niedostępna.[/bold red]")
            elif wybor_start_game == "3":
                clear_terminal()
                gracz_imie = 'Guest'
                poziom_trudnosci = wybierz_poziom_trudnosci()
                gracz = Gracz(gracz_imie, poziom_trudnosci)
                
                return gracz
            else:
                console.print("[bold red]Niepoprawny wybór. Spróbuj ponownie.[/bold red]")
        elif wybor == "2":
            clear_terminal()
            # Informacje o Grze
            informacje_o_grze()
        elif wybor == "3":
            clear_terminal()
            # Autorzy
            autorzy()
        else:
            console.print("[bold yellow]Niepoprawny wybór. Spróbuj ponownie.[/bold yellow]")
gracz = game_start()

while gracz.hp > 0:
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
        gracz.menu_gracza()
    elif wybor == "2":
        Podroz.menu_podrozy(gracz)  
    elif wybor == "3":
        Akcje.menu_akcji(gracz)  
    elif wybor == "4":
        console.print("[bold red]Dziękujemy za grę. Do zobaczenia![/bold red]")
        break
    elif wybor == "i":
        Inventory.inventory_menu(gracz)
    else:
        console.print("[bold yellow]Niepoprawny wybór. Spróbuj ponownie.[/bold yellow]")