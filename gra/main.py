#Wojtek i Aleks

# Importujemy klasy DaneGry, Gracz, inventorym fishing, mechaniki, akcje, podroz i Osada z odpowiednich plików
from dane import DaneGry
from gracz import Gracz
from osada import Osada
from inventory import inventory
from fishing import fishing
from podroz import podroz
from Akcje import akcje
from mechaniki import mechaniki
from enchanty import enchanty

# Funkcja tworząca nowego gracza i dokonująca przykładowego zakupu hełmu
def stworz_nowego_gracza(dane_gry):
    while True:
        imie = input("Podaj imię gracza: ")
        if imie.strip():  # Sprawdzamy, czy imię nie jest puste po usunięciu ewentualnych białych znaków
            break
        else:
            print("Imię nie może być puste. Spróbuj ponownie.")

    nowy_gracz = Gracz(imie)
    return nowy_gracz

# Główna pętla gry
nowy_gracz = stworz_nowego_gracza(DaneGry())  

while nowy_gracz.hp > 0:
    print("\n=== Główne Menu ===")
    print("1. Gracz")
    print("2. Podróże")
    print("3. Akcje")
    print("4. Wyjście")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        
        pass
    elif wybor == "2":
        # Implementacja opcji Podróże
        pass
    elif wybor == "3":
        # Implementacja opcji Akcje
        pass
    elif wybor == "4":
        # Zakończ program
        print("Dziękujemy za grę. Do zobaczenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
