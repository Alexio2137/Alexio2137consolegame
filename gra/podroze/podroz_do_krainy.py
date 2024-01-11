from dane import DaneGry
from gracz import Gracz

dane_gry = DaneGry()
# Wywołanie metody lokalizacje, która utworzy atrybut krainy
dane_gry.lokalizacje()

class PodrozDoKrainy:
    def menu_wyboru_krainy(self, dane_gry):
        print("Menu Wyboru Krainy:")
        for i, kraina in enumerate(dane_gry.krainy.keys(), 1):
            print(f"{i}. {kraina}")
        input("Naciśnij enter aby powrócić:  ")




