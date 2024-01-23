#Aleks

from rich.table import Table
from rich.console import Console
from rich import print as rprint
from dane import DaneGry
from dane import clear_terminal
from gracz import Gracz


console = Console()

def wyswietl_inventory(gracz):
    table = Table(show_lines=True)

    # Dodawanie kolumn do tabeli
    table.add_column("[cyan]Kategoria[/cyan]", style="bold cyan")
    table.add_column("[cyan]Nazwa[/cyan]", style="bold cyan")
    table.add_column("[cyan]Ilość[/cyan]", style="bold cyan")

    # Funkcja pomocnicza do dodawania wierszy do tabeli
    def add_rows(category, items):
        for item in items:
            if isinstance(item, dict):  
                nazwa = item.get('nazwa', '')
                ilosc = item.get('ilosc', 1)  # Domyślna ilość to 1, jeśli nie jest podana
                if isinstance(nazwa, str) and isinstance(ilosc, (int, float)):
                    table.add_row(category, nazwa, str(ilosc))
                else:
                    print(f"Błąd: Nieprawidłowy format elementu w kategorii '{category}'")
            else:
                print(f"Błąd: Nieprawidłowy format elementu w kategorii '{category}'")

    # Wyświetlanie rzeczy w ekwipunku
    for category, items in gracz.inventory['rzeczy'].items():
        add_rows(category.capitalize(), items)

    # Wyświetlanie picia
    add_rows("Picia", gracz.inventory['picia'])

    # Wyświetlanie jedzenia
    add_rows("Jedzenie", gracz.inventory['jedzenie'])

    # Wyświetlanie lootów
    add_rows("Looty", gracz.inventory['looty'])

    # Wyświetlanie stajni
    add_rows("Stajnia", gracz.inventory['stajnia'])

    # Wyświetlanie innych przedmiotów
    add_rows("Inne", gracz.inventory['inne'])

    # Wyświetlanie tabeli
    console.print(table)





class Inventory:
    def inventory_menu(gracz):
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
                wyswietl_inventory(gracz)
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
'''
def dodaj_do_wyposazenia(self, kategoria, item):
        if kategoria in self.wyposazenie and item is not None:
            # Sprawdzenie, czy gracz ma już coś w danym slocie
            if self.wyposazenie[kategoria] is None:
                self.wyposazenie[kategoria] = item
                print(f"[green]Założono: {item}[/green]")
            else:
                print("[bold yellow]Masz już coś założone w tym slocie. Zdejmij to wcześniej.[/bold yellow]")
        else:
            print("[bold yellow]Błąd: Nieprawidłowa kategoria lub przedmiot.[/bold yellow]")

    def zaloz_item(self):
        # Wyświetlanie ekwipunku przed wyborem
        wyswietl_inventory(self)

        # Pobranie kategorii i nazwy przedmiotu od gracza
        kategoria = input("Podaj kategorię przedmiotu do założenia: ").lower()
        nazwa_przedmiotu = input("Podaj nazwę przedmiotu do założenia: ")

        # Sprawdzenie, czy kategoria istnieje w ekwipunku gracza
        if kategoria in self.inventory['rzeczy']:
            items_w_kategorii = self.inventory['rzeczy'][kategoria]
            for item in items_w_kategorii:
                if item.get('nazwa') == nazwa_przedmiotu:
                    # Znaleziono przedmiot, można go założyć
                    self.dodaj_do_wyposazenia(kategoria, item)
                    break
            else:
                print("[bold yellow]Nie znaleziono podanego przedmiotu w ekwipunku.[/bold yellow]")
        else:
            print("[bold yellow]Podana kategoria nie istnieje w ekwipunku.[/bold yellow]")

    def sciagnij_z_wyposazenia(self, kategoria):
        if kategoria in self.wyposazenie:
            if self.wyposazenie[kategoria] is not None:
                print(f"[green]Ściągnięto: {self.wyposazenie[kategoria]}[/green]")
                self.wyposazenie[kategoria] = None
            else:
                print("[bold yellow]Nie masz niczego założonego w tym slocie.[/bold yellow]")
        else:
            print("[bold yellow]Błąd: Nieprawidłowa kategoria.[/bold yellow]")

    def wyrzuc_item(self, kategoria, nazwa_przedmiotu):
        if kategoria in self.inventory['rzeczy']:
            items_w_kategorii = self.inventory['rzeczy'][kategoria]
            for item in items_w_kategorii:
                if item.get('nazwa') == nazwa_przedmiotu:
                    # Znaleziono przedmiot, można go wyrzucić
                    items_w_kategorii.remove(item)
                    print(f"[magenta]Wyrzucono: {item}[/magenta]")
                    break
            else:
                print("[bold yellow]Nie znaleziono podanego przedmiotu w ekwipunku.[/bold yellow]")
        else:
            print("[bold yellow]Podana kategoria nie istnieje w ekwipunku.[/bold yellow]")



'''

