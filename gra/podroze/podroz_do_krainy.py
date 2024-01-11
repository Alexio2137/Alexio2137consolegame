from rich.console import Console
from rich.table import Table
from dane import DaneGry
from gracz import Gracz
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
    def menu_wyboru_krainy(self, dane_gry, gracz):
        print("Menu Wyboru Krainy:")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Numer", style="cyan")
        table.add_column("Kraina", style="cyan")

        for i, kraina in enumerate(dane_gry.krainy.keys(), 1):
            table.add_row(str(i), kraina)

        console.print(table)

        while True:
            wybor_krainy = input("Wybierz numer krainy, do której chcesz podróżować (lub wpisz 'q' aby powrócić): ")

            if wybor_krainy.lower() == 'q':
                break

            try:
                wybor_krainy = int(wybor_krainy)
                if 1 <= wybor_krainy <= len(dane_gry.krainy):
                    wybrana_kraina = list(dane_gry.krainy.keys())[wybor_krainy - 1]
                    console.print(f"Wybierasz podróż do krainy: [bold]{wybrana_kraina}[/bold]")

                    if wybrana_kraina in dane_gry.krainy:
                        self.menu_wybranej_krainy(wybrana_kraina, gracz)
                    else:
                        console.print("Nieprawidłowy numer krainy. Spróbuj ponownie.")
                else:
                    console.print("Nieprawidłowy numer krainy. Spróbuj ponownie.")
            except ValueError:
                console.print("Nieprawidłowe dane. Wprowadź poprawny numer krainy lub 'q' aby powrócić.")

    def menu_wybranej_krainy(self, wybrana_kraina, gracz):
        if wybrana_kraina == 'Wiecznie zielone łąki':
            self.menu_wiecznie_zielone_laki(gracz)
        elif wybrana_kraina == 'Przesadnie wysokie wyżyny':
            self.menu_przesadnie_wysokie_wyzimy(gracz)
        elif wybrana_kraina == 'Puszcza Reymlandzka':
            self.menu_puszcza_reymlandzka(gracz)
        elif wybrana_kraina == 'Thriller Bark':
            self.menu_thriller_bark(gracz)
        elif wybrana_kraina == 'Hueco Mundo':
            self.menu_hueco_mundo(gracz)
        elif wybrana_kraina == 'Góry Błękitnego Ognia':
            self.menu_gory_blekitnego_ognia(gracz)