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
    
    #Thriller Bark
        
    def bagno_dlugie_cienie(gracz):
        nazwa_lokacji = "Bagno Długie Cienie"
        opis_lokacji = "Trudne bagno, w którym cienie przybierają niepokojące formy. Miejsce pełne zagadek i niebezpieczeństw."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def cmentarz_wiecznych_swiatel(gracz):
        nazwa_lokacji = "Cmentarz Wiecznych Świateł"
        opis_lokacji = "Trudny cmentarz oświetlony niewyjaśnionymi światłami. Miejsce spoczywania dusz, które nigdy nie gasną."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def dolina_mrocznych_tajemnic(gracz):
        nazwa_lokacji = "Dolina Mrocznych Tajemnic"
        opis_lokacji = "Trudna dolina pełna nieznanych tajemnic. Miejsce, gdzie cienie ukrywają mroczne sekrety."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def grobowiec_zagubionych_dusz(gracz):
        nazwa_lokacji = "Grobowiec Zagubionych Dusz"
        opis_lokacji = "Bardzo trudny grobowiec, w którym spoczywają dusze bez świadomości. Miejsce pełne melancholii i rozpaczy."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def jama_malowanych_ciemnosci(gracz):
        nazwa_lokacji = "Jama Malowanych Ciemności"
        opis_lokacji = "Bardzo trudna jaskinia, gdzie cienie przybierają kolorowe i złowieszczne formy. Miejsce sztuki i mrocznej magii."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def jaskinia_zakletych_marzen(gracz):
        nazwa_lokacji = "Jaskinia Zaklętych Marzeń"
        opis_lokacji = "Bardzo trudna jaskinia, w której spełniają się i przekształcają marzenia. Miejsce pełne tajemniczych iluzji."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def opuszczona_kopalnia_mroku(gracz):
        nazwa_lokacji = "Opuszczona Kopalnia Mroku"
        opis_lokacji = "Bardzo trudna kopalnia, gdzie cienie ukrywają starożytne tajemnice. Miejsce zapomnianych bogactw i niebezpieczeństw."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def strumyk_zaginionych_nadziei(gracz):
        nazwa_lokacji = "Strumyk Zaginionych Nadziei"
        opis_lokacji = "Bardzo trudny strumyk, gdzie cienie oplatają zaginione nadzieje. Miejsce melancholii i utraconych marzeń."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def rezydencja_zlowrogich_duchow(gracz):
        nazwa_lokacji = "Rezydencja Złowrogich Duchów"
        opis_lokacji = "Bardzo trudna rezydencja, w której zjawa cieni przemykają między pokojami. Miejsce nawiedzonej przeszłości."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def grota_nocy(gracz):
        nazwa_lokacji = "Grota Nocy"
        opis_lokacji = "Bardzo trudna grota, w której cienie przybierają mroczne kształty. Miejsce pełne tajemniczych spisków i niebezpieczeństw."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    #Hueco Mundo
    def pustynia_rozpaczliwych_dusz(gracz):
        nazwa_lokacji = "Pustynia Rozpaczliwych Dusz"
        opis_lokacji = "Trudna pustynia, gdzie dusze cieni szukają spokoju. Miejsce przesiąknięte smutkiem i tajemnicami."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def jama_mrocznej_prozni(gracz):
        nazwa_lokacji = "Jama Mrocznej Próżni"
        opis_lokacji = "Trudna jama, gdzie cienie przenikają pustkę. Miejsce pełne nihilistycznej energii i mrocznych refleksji."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def jama_zadlacego_cienia(gracz):
        nazwa_lokacji = "Jama Żądlącego Cienia"
        opis_lokacji = "Trudna jama, gdzie cienie żądlące zło przemykają między skałami. Miejsce niebezpieczeństwa i ukrytych intryg."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def jama_pustki(gracz):
        nazwa_lokacji = "Jama Pustki"
        opis_lokacji = "Bardzo trudna jama, gdzie pustka pochłania światło. Miejsce, gdzie czas i przestrzeń tracą swoje znaczenie."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def ruiny_zapomnianej_chwaly(gracz):
        nazwa_lokacji = "Ruiny Zapomnianej Chwały"
        opis_lokacji = "Bardzo trudne ruiny, gdzie cienie minionych wielkości krążą. Miejsce zapomnianych podbojów i upadku."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def grota_plonacej_nocy(gracz):
        nazwa_lokacji = "Grota Płonącej Nocy"
        opis_lokacji = "Bardzo trudna grota, gdzie cienie płoną mrocznym ogniem. Miejsce wiecznego spopielenia i zniszczenia."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def pieklo_pustyni(gracz):
        nazwa_lokacji = "Piekło Pustyni"
        opis_lokacji = "Bardzo trudne piekło, gdzie cienie toną w morzu ognia. Miejsce wiecznego cierpienia i rozpaczy."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def krypta_zlowieszczej_pustki(gracz):
        nazwa_lokacji = "Krypta Złowieszczej Pustki"
        opis_lokacji = "Bardzo trudna krypta, gdzie cienie krążą wokół mrocznych tajemnic. Miejsce ukrytych koszmarów i złowrogiej pustki."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def zakrwawiony_plac(gracz):
        nazwa_lokacji = "Zakrwawiony Plac"
        opis_lokacji = "Bardzo trudny plac, gdzie cienie broczą krwią. Miejsce krwawych walk i zakazanych rytuałów."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def wyschniete_koryto(gracz):
        nazwa_lokacji = "Wyschnięte Koryto"
        opis_lokacji = "Bardzo trudne koryto rzeki, gdzie cienie suszą się w bezdennej pustce. Miejsce utraconej płynności i życia."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass
    
    #Góry Błękitnego Ognia
        
    def gora_plonacych_serc(gracz):
        nazwa_lokacji = "Góra Płonących Serc"
        opis_lokacji = "Średnia góra, gdzie płonące serca tchną życiem w skały. Miejsce namiętności i gorących emocji."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def gora_szmaragdowego_ognia(gracz):
        nazwa_lokacji = "Góra Szmaragdowego Ognia"
        opis_lokacji = "Średnia góra, gdzie szmaragdowy ogień tańczy między skałami. Miejsce zielonej magii i tajemniczych mocy."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def gora_dlony_krysztalow(gracz):
        nazwa_lokacji = "Góra Dłonięcia Kryształów"
        opis_lokacji = "Średnia góra, gdzie dłoniecia kryształów wznoszą się ku niebu. Miejsce magii kryształów i ich zaklętych tajemnic."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Średni", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def opuszczona_kopalnia_niebianskiego_blasku(gracz):
        nazwa_lokacji = "Opuszczona Kopalnia Niebiańskiego Blasku"
        opis_lokacji = "Trudna opuszczona kopalnia, gdzie niebiański blask niegdyś świecił. Miejsce zapomnianej świetności i ukrytych bogactw."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def wzgorze_blekitnych_marzen(gracz):
        nazwa_lokacji = "Wzgórze Błękitnych Marzeń"
        opis_lokacji = "Trudne wzgórze, gdzie marzenia unoszą się niczym chmury. Miejsce pragnień i ukrytych tajemnic."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def szczyt_wulkanu_nadziei(gracz):
        nazwa_lokacji = "Szczyt Wulkanu Nadziei"
        opis_lokacji = "Trudny szczyt wulkanu, gdzie nadzieja bucha niczym płomienie. Miejsce ognia i wznoszących się marzeń."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def lawa_i_kamienie_przeznaczenia(gracz):
        nazwa_lokacji = "Lawa i Kamienie Przeznaczenia"
        opis_lokacji = "Bardzo trudna kraina, gdzie lawa kształtuje kamienie przyszłości. Miejsce nieuchronnego przeznaczenia i rozstrzygających decyzji."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def kopalnia_krysztalow_utraconych_pran(gracz):
        nazwa_lokacji = "Kopalnia Kryształów Utraconych Pragnień"
        opis_lokacji = "Bardzo trudna kopalnia, gdzie kryształy skrywają utracone pragnienia. Miejsce zagubionych marzeń i kuszącej mocy."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def warownia_blekitnej_mocy(gracz):
        nazwa_lokacji = "Warownia Błękitnej Mocy"
        opis_lokacji = "Bardzo trudna warownia, gdzie błękitna moc czuwa nad krainą. Miejsce nieosiągalnych mocy i tajemniczych zaklęć."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass

    def kamienne_swiatynie_nadchodzacej_burzy(gracz):
        nazwa_lokacji = "Kamienne Świątynie Nadchodzącej Burzy"
        opis_lokacji = "Bardzo trudne kamienne świątynie, gdzie burza zbiera swoją moc. Miejsce nieokiełznanej natury i potężnych żywiołów."
        result = Lokacje_i_obiekty.dzialanie_lokacji(gracz, "Bardzo Trudny", random.randint(1, 3), random.randint(1, 3), random.randint(1, 5), nazwa_lokacji, opis_lokacji)

        if result:
            print('Akcja po wyborze "tak"')
        else:
            pass
