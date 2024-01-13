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




def menu_wybranej_krainy(wybrana_kraina, gracz):  # Added gracz parameter
        if wybrana_kraina == '1':
            menu_wiecznie_zielone_laki(gracz)
        elif wybrana_kraina == '2':
            menu_przesadnie_wysokie_wyzimy(gracz)
        elif wybrana_kraina == '3':
            menu_puszcza_reymlandzka(gracz)
        elif wybrana_kraina == '4':
            menu_thriller_bark(gracz)
        elif wybrana_kraina == '5':
            menu_hueco_mundo(gracz)
        elif wybrana_kraina == '6':
            menu_gory_blekitnego_ognia(gracz)



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
                        if wybrana_kraina == 'Wiecznie zielone łąki':
                            menu_wiecznie_zielone_laki(gracz)
                        elif wybrana_kraina == 'Przesadnie wysokie wyżyny':
                            menu_przesadnie_wysokie_wyzimy(gracz)
                        elif wybrana_kraina == 'Puszcza Reymlandzka':
                            menu_puszcza_reymlandzka(gracz)
                        elif wybrana_kraina == 'Thriller Bark':
                            menu_thriller_bark(gracz)
                        elif wybrana_kraina == 'Hueco Mundo':
                            menu_hueco_mundo(gracz)
                        elif wybrana_kraina == 'Góry Błękitnego Ognia':
                            menu_gory_blekitnego_ognia(gracz)
                        
                    else:
                        console.print("Nieprawidłowy numer krainy. Spróbuj ponownie.")
                else:
                    console.print("Nieprawidłowy numer krainy. Spróbuj ponownie.")
            except ValueError:
                console.print("Nieprawidłowe dane. Wprowadź poprawny numer krainy lub 'q' aby powrócić.")





    