#Mateusz

import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class DaneGry:
    def lokalizacje(self):
        self.krainy = {
        'kraj_A': {'opis': 'Opis kraju A', 'utrata staminy': 10},
        'kraj_B': {'opis': 'Opis kraju B', 'utrata staminy': 15},
        'kraj_C': {'opis': 'Opis kraju C', 'utrata staminy': 20},
        'kraj_D': {'opis': 'Opis kraju D', 'utrata staminy': 12},
        'kraj_E': {'opis': 'Opis kraju E', 'utrata staminy': 18},
        'kraj_F': {'opis': 'Opis kraju F', 'utrata staminy': 25},
        }

        #miejsce na lokalizacje
        self.lokalizacje = {
            'las': {'Opis': 'las'}
        }
        #miejsce na wioski miasta obozy
        self.osady = {
            'Miasta': {

            },
            'Wsie': {

            },
            'Osady': {

            },
            'Obozy': {

            }
        }
    def rzeczy(self):
        #miejsce na rzeczy z wyszczególnieniem na kategorie
        self.przedmioty = {
            'Hełmy': {
                'Hełm Żelazny': {'Opis': 'Solidny hełm z żelaza. Doskonała ochrona dla głowy w trakcie walki.', 'Wytrzymałość': 50, 'MaxWytrzymałość': 100, 'BonusAP': 5, 'BonusDP': 2, 'CenaKupna': 50, 'CenaSprzedazy': 25}
            },
            'Zbroje': {
                'Zbroja Skórzana': {'Opis': 'Lekka skórzana zbroja zapewniająca równowagę między ochroną a swobodą ruchów.', 'Wytrzymałość': 30, 'MaxWytrzymałość': 60, 'BonusAP': 2, 'BonusDP': 5, 'CenaKupna': 40, 'CenaSprzedazy': 20}
            },
            'Buty': {
                'Buty Lekkie': {'Opis': 'Lekkie buty zwiększające szybkość poruszania się, idealne dla szybkich i zwinnych wojowników.', 'Wytrzymałość': 20, 'MaxWytrzymałość': 40, 'BonusAP': 1, 'BonusDP': 1, 'CenaKupna': 30, 'CenaSprzedazy': 15}
            },
            'Rękawice': {
                'Rękawice Zbrojne': {'Opis': 'Rękawice wzmacniające siłę ataku, doskonałe dla tych, którzy cenią sobie agresywną walkę.', 'Wytrzymałość': 40, 'MaxWytrzymałość': 80, 'BonusAP': 3, 'BonusDP': 3, 'CenaKupna': 45, 'CenaSprzedazy': 22}
            },
            'Miecze': {
                'Miecz Krótki': {'Opis': 'Podstawowy miecz do walki wręcz, doskonały dla tych, którzy preferują szybkie ataki.', 'Wytrzymałość': 60, 'MaxWytrzymałość': 120, 'BonusAP': 8, 'BonusDP': 3, 'CenaKupna': 70, 'CenaSprzedazy': 35}
            },
            'Tarcze': {
                'Tarcza Drewniana': {'Opis': 'Drewniana tarcza zapewniająca solidną ochronę przed atakami wroga.', 'Wytrzymałość': 30, 'MaxWytrzymałość': 60, 'BonusAP': 1, 'BonusDP': 5, 'CenaKupna': 40, 'CenaSprzedazy': 20}
            },
            'Druga_Broń': {
                'Topór Dwuręczny': {'Opis': 'Potężny topór wymagający obu rąk do użycia, doskonały dla wojowników preferujących siłę nad zręcznością.', 'Wytrzymałość': 80, 'MaxWytrzymałość': 160, 'BonusAP': 10, 'BonusDP': 4, 'CenaKupna': 90, 'CenaSprzedazy': 45}
            }
        }

        self.potki = {
            'Lecznicze': {
                'Mikstura Leczenia': {'Opis': 'Mikstura lecząca obrażenia i przywracająca zdrowie. Idealna dla rannych wojowników na polu bitwy.', 'Odnawia_HP': 30, 'CenaKupna': 20, 'CenaSprzedazy': 10}
            },
            'Zwiększające_AP': {
                'Eliksir Mocy': {'Opis': 'Eliksir zwiększający punkty akcji (AP), pozwalający na bardziej wymagające ruchy w walce.', 'Dodaje_AP': 20, 'CenaKupna': 25, 'CenaSprzedazy': 12}
            },
            'Zwiększające_DP': {
                'Mikstura Obrony': {'Opis': 'Mikstura zwiększająca punkty obrony (DP), wzmacniająca pancerz przed atakami wrogów.', 'Dodaje_DP': 15, 'CenaKupna': 22, 'CenaSprzedazy': 11}
            },
            'Odnawiające_Energię': {
                'Napój Energizujący': {'Opis': 'Napój przywracający energię i redukujący zmęczenie, idealny dla wojowników potrzebujących dodatkowego zrywu.', 'Odnawia_Energie': 25, 'CenaKupna': 18, 'CenaSprzedazy': 9}
            }
        }
        #miejsce na jedzenie
        self.jedzenie = {
            'Mięso': {
                'Kiełbasa': {'Opis': 'Kiełbasa przyrządzona z różnych rodzajów mięsa. Smaczna przekąska na polu bitwy.', 'Odnawia_Głód': 15, 'Zabiera_Picie': 5, 'CenaKupna': 10, 'CenaSprzedazy': 5}
            },
            'Owoce': {
                'Jabłko': {'Opis': 'Świeże i soczyste jabłko. Zdrowa przekąska dla wędrowców.', 'Odnawia_Głód': 8, 'Dodaje_Picie': 10, 'CenaKupna': 6, 'CenaSprzedazy': 3}
            },
            'Warzywa': {
                'Marchewka': {'Opis': 'Chrunchy i zdrowy warzywny przysmak. Idealny dodatek do posiłku na szlaku.', 'Dodaje_Jedzenie': 10, 'Dodaje_Picie': 5, 'CenaKupna': 8, 'CenaSprzedazy': 4}
            }
        }
        #miejsce na picie
        self.picie = {
            'Woda': {
                'Woda Źródlana': {'Opis': 'Czysta woda ze źródła. Niezbędna dla każdego podróżującego.', 'Odnawia_Picie': 20, 'CenaKupna': 4, 'CenaSprzedazy': 2}
            },
            'Alkohole': {
                'Vódka': {'Opis': 'Dobra Polska Vódka', 'Odnawia_Picie': 5, 'CenaKupna': 20, 'CenaSprzedazy': 10}
            }
        }
        self.przedmioty = {
            'Siekiery': {

            },
            'Kilofy': {

            }
            #miejsce na rozój
        }
    def przeciwnicy(self):
        #miejsce na przeciwników
        self.przeciwnicy = {
            'Szkielety': {
                'Szkielet Wojownika': {'Opis': 'Nieumarły wojownik zbrojny w kościach. Poszukuj go w podziemiach grobowców.', 'Siła': 10, 'Obrona': 5, 'PunktyZdrowia': 30, 'Doświadczenie': 20, 'Złoto': 15}
            },
            'Gobliny': {
                'Goblin Łotrzyk': {'Opis': 'Mały i chytry goblin specjalizujący się w podstępach. Czai się w lasach i gęstwinach.', 'Siła': 5, 'Obrona': 2, 'PunktyZdrowia': 15, 'Doświadczenie': 10, 'Złoto': 8}
            },
            'Bandyci': {
                'Bandyta Łowca': {'Opis': 'Złoczyńca polujący na niewinnych podróżnych. Często spotykany na szlakach handlowych.', 'Siła': 12, 'Obrona': 7, 'PunktyZdrowia': 40, 'Doświadczenie': 25, 'Złoto': 20}
            }
        }
    def konie(self):
        self.konie = {
            'koń': {'opis: Coś tam, DodatkowaStamina': 10, 'CenaKupna': 8, 'CenaSprzedarzy': 5}
        }

# Utwórz instancję klasy DaneGry
dane_gry = DaneGry()
