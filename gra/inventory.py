#Wojtek

from rich.table import Table
from rich.console import Console
from rich import print as rprint
from dane import DaneGry
from dane import clear_terminal

console = Console()

class Inventory:
    def inventory_menu():
        while True:
            table = Table(show_lines=True)

            # Dodawanie kolumn do tabeli
            table.add_column("[cyan]# [/cyan]", justify="center", style="bold cyan")
            table.add_column("[cyan]Opcja[/cyan]", style="bold cyan")

            # Dodawanie danych do tabeli
            table.add_row("[yellow]1[/yellow]", "[yellow]Wyświetl menu[/yellow]")
            table.add_row("[yellow]2[/yellow]", "[green]Załóż item[/green]")
            table.add_row("[yellow]3[/yellow]", "[blue]Zdejmij item[/blue]")
            table.add_row("[yellow]4[/yellow]", "[magenta]Wyrzuć item[/magenta]")
            table.add_row("[yellow]5[/yellow]", "[red]Powrót[/red]")

            # Wyświetlanie tabeli
            console.print(table)
            
            wybor_inventory_menu = input("Wybór: ")

            if wybor_inventory_menu == '1':
                clear_terminal()
                print("[yellow]Wybrano opcję 1 - Wyświetl menu[/yellow]")
            elif wybor_inventory_menu == '2':
                clear_terminal()
                print("[green]Wybrano opcję 2 - Załóż item[/green]")
            elif wybor_inventory_menu == '3':
                clear_terminal()
                print("[blue]Wybrano opcję 3 - Zdejmij item[/blue]")
            elif wybor_inventory_menu == '4':
                clear_terminal()
                print("[magenta]Wybrano opcję 4 - Wyrzuć item[/magenta]")
            elif wybor_inventory_menu == '5':
                clear_terminal()
                print("[red]Wybrano opcję 5 - Powrót[/red]")
                break
            else:
                print("[bold yellow]Niepoprawny wybór. Spróbuj ponownie.[/bold yellow]")

# Przykład użycia

            
    # Do naprawy krecie!
    '''# def inventory():
        while True:
            table = PrettyTable()
        
            # Dodawanie kolumn do tabeli
            table.field_names = [colored("#", 'cyan'), colored("Rodzaj", 'cyan'), colored("Nazwa", 'cyan'), colored("Ilość", 'cyan')]

            # Dodawanie danych do tabeli
            table.add_row([colored("1", 'yellow'), colored("Hełmy", 'red')])
            table.add_row([colored("2", 'yellow'), colored("Zbroje", 'orange')])
            table.add_row([colored("3", 'yellow'), colored("Buty", 'yellow')])
            table.add_row([colored("4", 'yellow'), colored("Rękawice", 'green')])
            table.add_row([colored("5", 'yellow'), colored("Bronie", 'blue')])
            table.add_row([colored("6", 'yellow'), colored("Narzędzia", 'purple')])
            table.add_row([colored("7", 'yellow'), colored("Potki leczące", 'pink')])
            table.add_row([colored("8", 'yellow'), colored("Potki zwiększające ap", 'red')])
            table.add_row([colored("9", 'yellow'), colored("Potki zwiększające dp", 'orange')])
            table.add_row([colored("10", 'yellow'), colored("Potki odnawiające energie", 'yellow')])
            table.add_row([colored("11", 'yellow'), colored("Picia", 'green')])
            table.add_row([colored("12", 'yellow'), colored("Jedzenia", 'blue')])
            table.add_row([colored("13", 'yellow'), colored("Looty", 'purple')])
            table.add_row([colored("14", 'yellow'), colored("Potki odnawiające energie", 'pink')])
            table.add_row([colored("15", 'yellow'), colored("Stajnia", 'red')])
            table.add_row([colored("16", 'yellow'), colored("Inne", 'orange')])
            table.add_row([colored("17", 'yellow'), colored("Powrót", 'yellow')])

            print(table)'''