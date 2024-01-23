from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from dane import DaneGry
from gracz import Gracz
from dane import clear_terminal
import time
import random
from podroze.gory_blekitnego_ognia import menu_gory_blekitnego_ognia
from podroze.hueco_mundo import menu_hueco_mundo
from podroze.przsadnie_wysokie_wyzyny import menu_przesadnie_wysokie_wyzimy
from podroze.puszcza_reymlandzka import menu_puszcza_reymlandzka
from podroze.thriller_bark import menu_thriller_bark
from podroze.wiecznie_zielone_laki import menu_wiecznie_zielone_laki

dane_gry = DaneGry()
# Wywołanie metody lokalizacje, która utworzy atrybut krainy
dane_gry.lokalizacje()
console = Console()


class PodrozDoKrainy:

    
        
    def pasek_postepu_podrozy(self):
        clear_terminal()
        with Progress() as progress:
            task = progress.add_task("[cyan]Podróż do krainy:", total=random.randint(10, 25))

            while not progress.finished:
                progress.update(task, advance=1)
                time.sleep(0.2)  # Symulacja czasu podróży

        console.print("\nPodróż zakończona!")
        


    def wyswietl_informacje_o_krainie(self, kraina):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Atrybut", style="cyan")
        table.add_column("Wartość", style="cyan")

        for atrybut, wartosc in kraina.items():
            table.add_row(atrybut, str(wartosc))

        console.print(table)

    def menu_wyboru_krainy(self, dane_gry, gracz):
        while True:
            clear_terminal()
            print("Menu Wyboru Krainy:")

            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Numer", style="cyan")
            table.add_column("Kraina", style="cyan")

            for i, kraina in enumerate(dane_gry.krainy.keys(), 1):
                table.add_row(str(i), kraina)

            console.print(table)

        
            wybor_krainy = input("Wybierz numer krainy, do której chcesz podróżować (lub wpisz 'q' aby powrócić): ")

            if wybor_krainy.lower() == 'q':
                break

            try:
                wybor_krainy = int(wybor_krainy)
                if 1 <= wybor_krainy <= len(dane_gry.krainy):
                    wybrana_kraina = list(dane_gry.krainy.keys())[wybor_krainy - 1]
                    console.print(f"Przed podróżą do krainy: [bold]{wybrana_kraina}[/bold]")
                    clear_terminal()
                    self.wyswietl_informacje_o_krainie(dane_gry.krainy[wybrana_kraina])

                    decyzja = input("Czy chcesz tam się udać? (tak/nie): ").lower()
                    if decyzja == 'tak':
                        utrata_staminy = dane_gry.krainy[wybrana_kraina]['utrata staminy']
                        if gracz.stamina >= utrata_staminy:
                            gracz.odejmij_stamine(utrata_staminy)
                        if wybrana_kraina == 'Wiecznie zielone łąki':
                            clear_terminal()
                            self.pasek_postepu_podrozy()
                            menu_wiecznie_zielone_laki(gracz)
                        elif wybrana_kraina == 'Przesadnie wysokie wyżyny':
                            clear_terminal()
                            self.pasek_postepu_podrozy()
                            menu_przesadnie_wysokie_wyzimy(gracz)
                        elif wybrana_kraina == 'Puszcza Reymlandzka':
                            clear_terminal()
                            self.pasek_postepu_podrozy()
                            menu_puszcza_reymlandzka(gracz)
                        elif wybrana_kraina == 'Thriller Bark':
                            clear_terminal()
                            self.pasek_postepu_podrozy()
                            menu_thriller_bark(gracz)
                        elif wybrana_kraina == 'Hueco Mundo':
                            clear_terminal()
                            self.pasek_postepu_podrozy()
                            menu_hueco_mundo(gracz)
                        elif wybrana_kraina == 'Góry Błękitnego Ognia':
                            clear_terminal()
                            self.pasek_postepu_podrozy()
                            menu_gory_blekitnego_ognia(gracz)
                        else:
                            console.print(f"{gracz.imie} nie ma wystarczającej ilości staminy do podróży.")
                    else:
                        console.print("Zawracasz przed podróżą.")
                else:
                    console.print("Nieprawidłowy numer krainy. Spróbuj ponownie.")
            except ValueError:
                console.print("Nieprawidłowe dane. Wprowadź poprawny numer krainy lub 'q' aby powrócić.")
