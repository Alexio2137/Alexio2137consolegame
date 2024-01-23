from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
import time
from dane import clear_terminal
import random
from Akcje import Akcje

console = Console()

class Lokacje_i_obiekty:
    def dzialanie_lokacji(gracz, ilosc_jedzenia, ilosc_pragnienia, ilosc_xp, nazwa_lokacji, opis_lokacji):
        console.clear()

        # Odejmowanie jedzenia i pragnienia
        gracz.odejmij_glod(ilosc_jedzenia)
        gracz.odejmij_picie(ilosc_pragnienia)

        # Dodawanie XP
        gracz.zwieksz_poziom(ilosc_xp)

        # Wyświetlanie komunikatu
        panel_data = [
            ["Ilość jedzenia", str(ilosc_jedzenia)],
            ["Ilość pragnienia", str(ilosc_pragnienia)],
            ["Ilość XP", str(ilosc_xp)],
            ["Nazwa lokacji", nazwa_lokacji],
            ["Opis lokacji", opis_lokacji],
        ]

        panel_table = Panel.fit_table(panel_data, title=f"[bold magenta]{nazwa_lokacji}[/bold magenta]", border_style="bold cyan")
        console.print(panel_table)

        while True:
            # Wybór gracza
            wybor = input("Czy chcesz pozostać na tej lokacji? (tak/nie): ").lower()

            if wybor == 'tak':
                return True
            elif wybor == 'nie':
                return False
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
                time.sleep(2)


    #Wiecznie zielone łąki

    def polana_kwitnacych_roz(gracz):
        nazwa_lokacji = "Polana Kwitnących Róż"
        opis_lokacji = "Urokliwa polana pełna różnokolorowych róż, które tańczą w rytm delikatnego wiatru. Doskonałe miejsce do wypoczynku."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Łatwy", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def las_delikatnych_lisci(gracz):
        nazwa_lokacji = "Las Delikatnych Liści"
        opis_lokacji = "Las, w którym drzewa posiadają delikatne liście, a ziemia pokryta jest miękkim mchem. Spokojne miejsce do eksploracji."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Łatwy", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def wzgorze_slonecznych_promieni(gracz):
        nazwa_lokacji = "Wzgórze Słonecznych Promieni"
        opis_lokacji = "Wzniesienie, z którego roztacza się widok na pełne słońca krajobrazy. Doskonałe miejsce na medytację."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Łatwy", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def zagroda_zycia(gracz):
        nazwa_lokacji = "Zagroda Życia"
        opis_lokacji = "Bezpieczna zagroda, gdzie zwierzęta żyją w zgodzie z przyrodą. Idealne miejsce na zbieranie surowców."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Łatwy", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def osada_pastoralna_marzenia(gracz):
        nazwa_lokacji = "Osada Pastoralna Marzenia"
        opis_lokacji = "Urokliwa osada, gdzie mieszkańcy realizują swoje marzenia. Znajdziesz tu ciekawych handlarzy i przyjaznych ludzi."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def zielona_laka_harmonii(gracz):
        nazwa_lokacji = "Zielona Łąka Harmonii"
        opis_lokacji = "Przestronna łąka, na której panuje harmonia między przyrodą a stworzeniami. Idealne miejsce do odpoczynku."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def sad_kwitnacych_drzew(gracz):
        nazwa_lokacji = "Sad Kwitnących Drzew"
        opis_lokacji = "Zadrzewiony obszar, na którym kwitną różnorodne drzewa. Miejsce pełne życia i piękna."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def gaj_kwiatowych_marzen(gracz):
        nazwa_lokacji = "Gaj Kwiatowych Marzeń"
        opis_lokacji = "Mały gaj, gdzie każdy kwiat to spełnione marzenie. Miejsce pełne magii i tajemnic."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def laka_kwiatowa_rozkoszy(gracz):
        nazwa_lokacji = "Łąka Kwiatowa Rozkoszy"
        opis_lokacji = "Trudno dostępna łąka, na której rosną rzadkie i piękne kwiaty. Miejsce wymagające odwagi i determinacji."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def skarpa_wiecznej_zieleni(gracz):
        nazwa_lokacji = "Skarpa Wiecznej Zieleni"
        opis_lokacji = "Stroma skarpa, gdzie rosną wiecznie zielone rośliny. Miejsce dla tych, którzy szukają wyzwań i przygód."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    #Przesadnie wysokie wyżyny
    
    def gora_spiewajacych_wiatrow(gracz):
        nazwa_lokacji = "Góra Śpiewających Wiatrów"
        opis_lokacji = "Majestatyczna góra, na której wiatr wydaje melodyczne dźwięki. Średnie wyzwanie dla śmiałków."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def przelecz_ognistego_nieba(gracz):
        nazwa_lokacji = "Przełęcz Ognistego Nieba"
        opis_lokacji = "Miejsce, gdzie ogniste zorze tańczą na niebie. Średnie wyzwanie dla śmiałków."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def klif_wieczornej_chwaly(gracz):
        nazwa_lokacji = "Klif Wieczornej Chwały"
        opis_lokacji = "Trudny teren, na którym chwała jest osiągalna tylko dla najwytrwalszych."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def szczyt_gorski_nadziei(gracz):
        nazwa_lokacji = "Szczyt Górski Nadziei"
        opis_lokacji = "Wierzchołek góry, gdzie nadzieja jest silniejsza niż gdziekolwiek indziej. Wyzwanie dla odważnych."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def wodospad_melodii(gracz):
        nazwa_lokacji = "Wodospad Melodii"
        opis_lokacji = "Trudny teren, gdzie wodospad wydaje melodyczne dźwięki. Dla tych, którzy kochają muzykę."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def spekane_skały_dzwiekow(gracz):
        nazwa_lokacji = "Spękane Skały Dźwięków"
        opis_lokacji = "Bardzo trudne tereny, gdzie skały wydają dźwięki pod wpływem magicznych sił."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def skalna_tarcza_mroznych_wiatrow(gracz):
        nazwa_lokacji = "Skalna Tarcza Mroźnych Wiatrów"
        opis_lokacji = "Bardzo trudny teren, gdzie lodowate wiatry tworzą tarczę. Tylko dla odważnych poszukiwaczy przygód."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def chata_lowcy_zagubionych_czasow(gracz):
        nazwa_lokacji = "Chata Łowcy Zagubionych Czasów"
        opis_lokacji = "Bardzo trudne miejsce, gdzie czas zdaje się biec inaczej. Tylko dla najodważniejszych poszukiwaczy."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def fort_obronny_zlotej_er(gracz):
        nazwa_lokacji = "Fort Obronny Złotej Er"
        opis_lokacji = "Bardzo trudny fort, w którym mieszkańcy bronią się przed złem. Wyzwanie dla odważnych wojowników."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def krysztalowy_dwor(gracz):
        nazwa_lokacji = "Kryształowy Dwór"
        opis_lokacji = "Bardzo trudne miejsce, gdzie każdy kryształ ma swoją historię. Dla tych, którzy gotowi są na prawdziwe wyzwanie."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass
    
    #Puszcza Reymlandzka
    
    
    def bagno_kwiecistych_trzcin(gracz):
        nazwa_lokacji = "Bagno Kwiecistych Trzcin"
        opis_lokacji = "Łatwe bagno pełne kwiecistych trzcin. Doskonałe dla nowicjuszy poszukiwaczy przygód."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Łatwy", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def bagno_spiewajacych_zab(gracz):
        nazwa_lokacji = "Bagno Śpiewających Żab"
        opis_lokacji = "Łatwe bagno, gdzie żaby sprawiają, że otoczenie wypełnia się muzyką. Idealne dla miłośników natury."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Łatwy", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def bagno_dlugie_cienie(gracz):
        nazwa_lokacji = "Bagno Długie Cienie"
        opis_lokacji = "Łatwe bagno, gdzie cienie wydają się być dłuższe niż zazwyczaj. Miejsce tajemnicze i pełne zagadek."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Łatwy", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def cmentarz_malowniczych_kamieni(gracz):
        nazwa_lokacji = "Cmentarz Malowniczych Kamieni"
        opis_lokacji = "Średni cmentarz, na którym kamienie przybierają malownicze formy. Miejsce pełne historii."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def cmentarz_swietnych_dusz(gracz):
        nazwa_lokacji = "Cmentarz Świętych Dusz"
        opis_lokacji = "Średni cmentarz, gdzie spoczywają duchy świętych. Miejsce wzbudzające szacunek i zadumę."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def dolina_mistycznego_czasu(gracz):
        nazwa_lokacji = "Dolina Mistycznego Czasu"
        opis_lokacji = "Średnia dolina, w której czas zdaje się płynąć inaczej. Miejsce pełne tajemnic i magii."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def las_szeptow_natury(gracz):
        nazwa_lokacji = "Las Szeptów Natury"
        opis_lokacji = "Średni las, w którym drzewa zdają się szeptać do podróżników. Miejsce spokojne i ożywione."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def jaskinia_lsnacych_skarbow(gracz):
        nazwa_lokacji = "Jaskinia Lśniących Skarbów"
        opis_lokacji = "Średnia jaskinia, w której skarby błyszczą niczym gwiazdy. Miejsce kuszące dla poszukiwaczy bogactw."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def staw_laskoczacych_roz(gracz):
        nazwa_lokacji = "Staw Łaskoczących Róż"
        opis_lokacji = "Trudny staw, w którym różowe płatki tańczą na powierzchni wody. Miejsce romantyczne, ale pełne niespodzianek."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def staw_dloniecia_zorzy(gracz):
        nazwa_lokacji = "Staw Dłonięcia Zorzy"
        opis_lokacji = "Bardzo trudny staw, gdzie zorze dłonięte są w wodzie. Miejsce magiczne, ale wymagające odwagi."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass
    
    def wioska_zapomnianych_dusz(gracz):
        nazwa_lokacji = "Wioska Zapomnianych Dusz"
        opis_lokacji = "Bardzo trudna wioska, w której zamieszkują zapomniane dusze. Miejsce pełne tajemnic i melancholii."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def wyspa_mgiel_i_marzen(gracz):
        nazwa_lokacji = "Wyspa Mgieł i Marzeń"
        opis_lokacji = "Bardzo trudna wyspa otulona mgiełką, na której spełniają się marzenia. Miejsce magiczne, ale niebezpieczne."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass