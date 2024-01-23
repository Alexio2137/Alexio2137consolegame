#Aleks i Wojtek
from rich.console import Console
from rich.table import Table
from dane import clear_terminal
from dane import DaneGry

console = Console()


def odpocznij():
    print("Odpoczywaj. Zregeneruj siły.")
    input("Naciśnij enter aby powrócić:  ")

def zjedz():
    print("Zjedz coś smacznego. Poczęstuj się posiłkiem.")
    input("Naciśnij enter aby powrócić:  ")

def napij_sie():
    print("Napij się, by ugasić pragnienie.")
    input("Naciśnij enter aby powrócić:  ")


def informacje_o_grze():
    table = Table(title="Mroczne Przejścia", title_style="bold magenta")
    table.add_row("[italic]Eksplozja Handlu i Wojenne Wyprawy[/italic]")
    table.add_row("[bold blue]Gra RPG tekstowa, gdzie podejmujesz decyzje i eksplorujesz świat.[/bold blue]")

    console.clear()
    console.print(table)
    input("Kliknij enter aby powrucić")

def autorzy():
    table = Table(title="Autorzy")
    table.add_column("Imię", style="bold")
    table.add_column("Nazwisko", style="bold")

    authors_data = [
        ("Aleks"),
        ("Mateusz"),
        ("Wojtek"),
    ]

    for author in authors_data:
        table.add_row(*author)

    clear_terminal()
    console.print(table)
    input("Kliknij enter aby powrucić")