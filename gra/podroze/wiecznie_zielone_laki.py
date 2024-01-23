from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
import time
from dane import clear_terminal
console = Console()
import random
from podroze.lokacje import Lokacje_i_obiekty
from Akcje import Akcje


def menu_wiecznie_zielone_laki(gracz):
    while True:

        def pasek_postepu_podrozy_wzl():
            clear_terminal()
            with Progress() as progress:
                task = progress.add_task("[cyan]Podróżujesz po krajinie:", total=random.randint(10, 25))

                while not progress.finished:
                    progress.update(task, advance=1)
                    time.sleep(0.2)  # Symulacja czasu podróży

        console.print("\nPodróż zakończona!")

        def losowa_lokacja():
            lokalizacje = {
                "bagno_male": 10,
                "bagno_srednie": 15,
                "cmentarz_maly": 5,
                "brak": 20
            }
            wybrana_lokacja = random.choices(list(lokalizacje.keys()), weights=lokalizacje.values(), k=1)[0]
            return getattr(Lokacje_i_obiekty, wybrana_lokacja)

        console.clear()

        table_info = Table(title="Wiecznie zielone łąki", show_header=False, header_style="bold magenta")
        table_info.add_column('Atrybut', style="cyan")
        table_info.add_column('Wartość', style="cyan")
        table_info.add_row('Punkty życia (HP)', f"[red]{gracz.hp}[/red]")
        table_info.add_row('Poziom wytrzymałości', f"[green]{gracz.stamina}[/green]")
        table_info.add_row('Poziom energii', f"[red]{gracz.energia}[/red]")
        table_info.add_row('Poziom głodu', f"[red]{gracz.effekty['glod']}[/red]")
        table_info.add_row('Poziom napojenia', f"[red]{gracz.effekty['pragnienie']}[/red]")

        table_options = Table(title="Dostępne opcje", show_header=False, header_style="bold cyan")
        table_options.add_column('Numer', style="cyan")
        table_options.add_column('Akcja', style="cyan")
        table_options.add_row('[cyan]1[/cyan]', 'Informacje o graczu')
        table_options.add_row('[cyan]2[/cyan]', 'Akcje')
        table_options.add_row('[cyan]3[/cyan]', 'Podróż po krainie')
        table_options.add_row('[cyan]4[/cyan]', 'Opuść krainę')

        console.print(Panel.fit(table_info, title="Wiecznie zielone łąki", border_style="bold magenta"))
        console.print(Panel.fit(table_options, title="Dostępne opcje", border_style="bold cyan"))

        try:
            wybor = int(input("Wybierz numer opcji: "))
            if wybor == 1:
                gracz.menu_gracza()
            elif wybor == 2:
                Akcje.menu_akcji(gracz)
            elif wybor == 3:
                lokacja = losowa_lokacja()
                if gracz.stamina >= 20:
                    utrata_staminy = random.randint(3, 5)
                    gracz.odejmij_stamine(utrata_staminy)
                    console.print(f"Utrata staminy: [bold]{utrata_staminy}[/bold]")
                    pasek_postepu_podrozy_wzl()
                    console.print(f"Przenoszenie do: [bold]{lokacja.__name__}[/bold]")
                    getattr(Lokacje_i_obiekty, lokacja.__name__)(gracz)
                else:
                    print("Masz za mało staminy")
            elif wybor == 4:
                break
            else:
                console.print("Nieprawidłowy numer opcji. Spróbuj ponownie.", style="bold red")
        except ValueError:
            console.print("Wprowadź poprawny numer opcji.", style="bold red")

