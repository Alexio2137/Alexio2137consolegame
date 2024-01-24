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


def menu_hueco_mundo(gracz):
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
                "Pustynia Rozpaczliwych Dusz": 15,
                "Jama Mrocznej Prozni": 15,
                "Jama Zadlacego Cienia": 15,
                "Jama Pustki": 10,
                "Ruiny Zapomnianej Chwaly": 10,
                "Grota Plonacej Nocy": 10,
                "Pieklo Pustyni": 10,
                "Krypta Zlowieszczej Pustki": 5,
                "Zakrwawiony Plac": 5,
                "Wyschniete Koryto": 5
            }

            wybrana_lokacja = random.choices(list(lokalizacje.keys()), weights=lokalizacje.values(), k=1)[0]

            # Zmiana spacji na podkreślenie w nazwie lokacji
            wybrana_lokacja_atrybut = wybrana_lokacja.lower().replace(" ", "_")

            # Teraz sprawdzamy, czy taki atrybut istnieje w Lokacje_i_obiekty
            if hasattr(Lokacje_i_obiekty, wybrana_lokacja_atrybut):
                lokacja = getattr(Lokacje_i_obiekty, wybrana_lokacja_atrybut)
                return lokacja
            else:
                print(f"Nie znaleziono lokacji o nazwie: {wybrana_lokacja}")
                return None

        console.clear()

        table_info = Table(title="Hueco Mundo", show_header=False, header_style="bold magenta")
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

        console.print(Panel.fit(table_info, title="Hueco Mundo", border_style="bold magenta"))
        console.print(Panel.fit(table_options, title="Dostępne opcje", border_style="bold cyan"))

        try:
            numer_opcji = int(input("Wybierz numer opcji: "))
            if numer_opcji == 1:
                gracz.menu_gracza()
            elif numer_opcji == 2:
                Akcje.menu_akcji(gracz)
            elif numer_opcji == 3:
                lokacja = losowa_lokacja()
                if gracz.stamina >= 20 and lokacja is not None:
                    utrata_staminy = random.randint(3, 5)
                    gracz.odejmij_stamine(utrata_staminy)
                    console.print(f"Utrata staminy: [bold]{utrata_staminy}[/bold]")
                    pasek_postepu_podrozy_wzl()
                    console.print(f"Przenoszenie do: [bold]{lokacja.__name__}[/bold]")  # Użyj __name__ aby uzyskać nazwę funkcji
                    lokacja(gracz)
                elif lokacja is None:
                    print("Nie udało się znaleźć lokacji.")
                else:
                    print("Masz za mało staminy")
            elif numer_opcji == 4:
                break
            else:
                console.print("Nieprawidłowy numer opcji. Spróbuj ponownie.", style="bold red")
        except ValueError:
            console.print("Wprowadź poprawny numer opcji.", style="bold red")