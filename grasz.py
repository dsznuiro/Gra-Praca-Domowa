import random
import time
import sys

#Oszczędza dużo miejsca, a tekst wtedy jest bardziej przystępny
def przerwa_print(tekst, opoznienie):
    print(tekst)
    time.sleep(opoznienie)

#Przyda sie do formatowanie tekstu. Można było użyć import os i os.get_terminal_size() ale wiem że nie działa to dla przykładu w pycharmie
szerokosc = 80

#Dlugie dialogi (zostawienie ich w środku kodu wprowadzilo by chaos)

wstep = ("Witaj! Gra, w którą zamierzasz zagrać, opiera się na elementach losowości. \n"
         "Porażki są nieuniknione, a dzięki różnym zakończeniom i innym mechanizmom, \n"
         "gra pozwala na wielokrotne przechodzenie różnych ścieżek. \n")

poradnik = ("Podczas gry natkniesz się na możliwość dokonania wyborów, które będą przedstawiane w następujący sposób: \n"
"[1] przedmiot1 \n"
"[2] przedmiot2 \n"
"[3] przedmiot3 \n"
"Jeśli chcesz wybrać przedmiot, możesz to zrobić, wpisując odpowiednią cyfrę, odpowiadającą mu, np. 1, lub wpisując nazwę owego przedmiotu. \n")

prolog = (
    "\n Szkocja pogrąża się w kryzysie, wywołanym niestabilnością rządów. Szansą na zjednoczenie kraju jest szanowany baron Durandal, \n"
    "który jednak zostaje porwany w tajemniczych okolicznościach. Jego brat, Roland [TY], wraz z dwójką wiernych rycerzy wyrusza na misję ratunkową. \n"
    "Ślady koniów prowadzą was do tajemniczego zamku, który nie znajduje się na żadnych mapach. \n"
    "Co więcej, zamek nie nosi żadnych znaków świadczących o przynależności do Anglii, ani tym bardziej do Szkocji... \n")

wejscie_do_zamku = ("Pomimo wielkiego ryzyka postanawiacie wejść do zamku, ponieważ złamaliście rozkaz rycerski i szukacie go na własną rękę, \n"
                    " ku zaskoczeniu od razu po wejściu do środka czujesz się słabo, słychać krzyki twoich kompanów a po chwili zapada cisza... \n"
)

unikniecie_smierci = [
"Czujesz ból, jakiego nie byłeś sobie wstanie kiedykolwiek wyobrazić....\n",
"Słyszysz głos cierpienia, jakiego nie byłeś sobie wstanie kiedykolwiek wyobrazić....\n",
"Ale... ten głos, choć znajomy nie jest twój...\n",
"To głos twojego brata...\n",
"Nagle widzisz blask światła potwór, z którym walczyłeś zniknął\n",
"Odzyskujesz swoje siły i idziesz dalej uratować Durandala!\n"
]

#zmienne wystepujące w gre

#statystyki
wytrzymalosc = 10
obrazenia = 30
szczescie = 12
dodatkowe_zycie = 1

#wrogowie dzięki temu potwory mogą być losowane z dostępnej puli
wrogowie = [
    {"potwor": "kamienny golem", "punkty zdrowia potwora": 200, "obrazenia potwora": 10},
    {"potwor": "duch poległego rycerza", "punkty zdrowia potwora": 100, "obrazenia potwora": 15},
    {"potwor": "szkielet z mieczem", "punkty zdrowia potwora": 50, "obrazenia potwora": 20},
    {"potwor": "skrzat z sakiewką", "punkty zdrowia potwora": 20, "obrazenia potwora": 5}
]

#pokoje
pokoj_z_potworem = 0
pokoj_na_klucz = 0
pokoj = 0

#inne
poziom_trudnosci = 0
liczba_kluczy = 0

#bronie
bron = 0
rapier = 0
luk = 0

przerwa_print(wstep, 4)
input("Naciśnij enter aby kontynuować... \n")
print("Ważne informacje: ".center(szerokosc))
przerwa_print(poradnik, 4)
input("Naciśnij enter aby kontynuować... \n")

przerwa_print("Czas: XII wiek".center(szerokosc), 1)
przerwa_print("Lokalizacja: Szkocja".center(szerokosc), 1)
przerwa_print("Tło historyczne: Kryzys wewnętrzny w Szkocji oraz wojna szkocko-angielska".center(szerokosc), 2)


przerwa_print(prolog, 4)

przerwa_print(wejscie_do_zamku, 3)
input("Naciśnij enter aby kontynuować... \n")

#Wybór poziomu trudności który opiera się o inną wartość punktów życia
print("Wybierz poziom trudnosci: ")
print("[1] Łatwy")
print("[2] Średni")
print("[3] Trudny")

while poziom_trudnosci not in ["1", "2", "3", "łatwy", "średni", "trudny"]:

    poziom_trudnosci = input().lower()
    if(poziom_trudnosci == "1" or poziom_trudnosci == "łatwy"):
        print("Wstajesz żwawo, nie czujesz, żebyś odniósł żadnych obrażeń.")
        punkty_zycia_bohatera = 60
    elif(poziom_trudnosci == "2" or poziom_trudnosci == "średni"):
        print("Wstajesz obolały, obrażenia są raczej powierzchowne.")
        punkty_zycia_bohatera = 35
    elif(poziom_trudnosci == "3" or poziom_trudnosci == "trudny"):
        print("Wstajesz ledwo żywy, czujesz tak ogromny ból, że nie wiesz, czy śmierć nie byłaby lepszą opcją.")
        punkty_zycia_bohatera = 20
    else: print("Niepoprawne dane. Spróbuj jeszcze raz! ")

time.sleep(4)
przerwa_print("Znajdujesz się w ciemnym budynku zamku, w którym cuchnie rozkładającym się zwłokami... \n",2)
przerwa_print("Widzisz pełno zbroi rycerskich, zarówno Anglików, jak i Szkotów a w środku ich coś, co tylko już przypomina ciało ludzkie...\n", 2)
przerwa_print("Znajdujesz swoich kompanów, którzy są martwi a obok nich leżą wasze bronie...\n", 2)

print("Wybierz broń: ")
print("[1] Dwuręczny miecz")
print("[2] Rapier")
print("[3] Łuk")
print("Aby otrzymać szczegółowe informacje o broniach napisz: [4] info")

#Wybór broni
while True:

    bron = input().lower()
    if(bron == "1" or bron == "dwuręczny miecz"):
        print("Podnosisz miecz, czujesz się znacznie silniejszy i pewny siebie.")
        bron = "dwuręczny miecz"
        wytrzymalosc += 20
        obrazenia += 17
        break
    elif (bron == "2" or bron == "rapier"):
        print("Podnosisz rapier, jego lekkość i elastyczność przy wykonywaniu ruchów daje ci otuchy.")
        bron = "rapier"
        szczescie *= 2
        break
    elif(bron == "3" or bron == "łuk"):
        print("Podnosisz łuk, słabniesz na bliski dystans lecz masz szanse wygrać na odległość.")
        bron = "łuk"
        wytrzymalosc -= 20
        obrazenia -= 5
        szczescie *= 1.3
        punkty_zycia_bohatera += 5
        break
    elif(bron == "4" or bron == "info"):
        przerwa_print("Każda z broni zapewnia ci różne statystyki: ", 1)
        przerwa_print("Dwuręczny miecz: zwiększa wyrzymałość oraz obrażenia", 1)
        przerwa_print("Rapier: zwiększa szczęście", 1)
        przerwa_print("Łuk: zwiększa szczęście oraz punkty życia ale redukuje wyrzymałość oraz obrażenia", 1)
    else: print("Niepoprawne dane. Spróbuj jeszcze raz! ")

time.sleep(2)
print(f"Masz {round(punkty_zycia_bohatera)} punktów życia!")
print("Przed sobą widzisz dwa pokoje jeden zamknięty na klucz a drugi otwarty, możesz dostrzec w nim tajemniczą sylwetke")

losowy_potwor = random.choice(wrogowie)

# Funkcja zwraca punkty zycia potworom po ich pokonaniu, bez tego występował problem że gdy losował sie dwa razy ten sam potwór to miał 0 punktów życia lub ujemne
def powrot_punktow_zdrowia_potwora():
    if losowy_potwor["potwor"] == "kamienny golem":
        losowy_potwor["punkty zdrowia potwora"] = 200
    elif losowy_potwor["potwor"] == "duch poległego rycerza":
        losowy_potwor["punkty zdrowia potwora"] = 100
    elif losowy_potwor["potwor"] == "szkielet z mieczem":
        losowy_potwor["punkty zdrowia potwora"] = 50
    else:
        losowy_potwor["punkty zdrowia potwora"] = 20


#trafienie krytyczne mechanika
#sczęścię zwiększa szansę na trafienie krytyczne oraz jego obrażenia
def szansza_krytyczna():
    if random.randint(0, round(100 - szczescie)) <= 30:
        return obrazenia * (1.3 + random.randint(0, int(szczescie * 0.1)))
    else:
        return 0

#mechanik broni specjalnych
#rapier ma szanse na uderzenie do 4 razy i każde obrażenie kolejnego pchnięcia maleją
def atak_rapiera():
    global pchniecia
    obrazenia_rapiera = 0
    pchniecia = 1
    while random.randint(0, 4 - pchniecia) <= 3 - pchniecia and pchniecia <= 4:
        obrazenia_rapiera += obrazenia * (4 - pchniecia) * 0.25
        pchniecia += 1
    return obrazenia_rapiera

#bohater z łukiem ma 1/3 szans na całkowite uniknięcie obrażeń, jeśli nie to dostaje zredukowane obrażenia o 0.3
def luk_odskok():
    global bron
    global obrazenia
    global wytrzymalosc
    global pchniecia
    global punkty_zycia_bohatera
    global losowy_potwor
    if random.randint(0,2) == 2:
        przerwa_print("Wykonujesz odskok, potwór próbuje cie uderzyć i...", 1)
        przerwa_print("Nie trafia, unikasz otrzymania obrażeń!", 1)
    else:
        punkty_zycia_bohatera -= round(losowy_potwor["obrazenia potwora"] * (1 - wytrzymalosc * 0.01)) * 0.3
        time.sleep(1)
        przerwa_print("Wykonujesz odskok, potwór próbuje cie uderzyć i...",1)
        przerwa_print("Trafia, ale otrzymujesz zredukowane obrażenia!",1)
        przerwa_print(f"Otrzymujesz {round(losowy_potwor['obrazenia potwora'] * (1 - wytrzymalosc * 0.01) * 0.3)} obrażeń!",1)
        przerwa_print(f"Masz teraz {round(punkty_zycia_bohatera)} punktów zdrowia!",1)

#dwuręczny miecz ma poprostu większe obrażenia ale mniejsze obrażenia z trafień krytycznych
def rodzaj_broni():
    global bron
    global obrazenia
    global wytrzymalosc
    global pchniecia
    global punkty_zycia_bohatera
    global losowy_potwor
    if bron == "dwuręczny miecz":
        losowy_potwor["punkty zdrowia potwora"] -= round( obrazenia * 1.6 + szansza_krytyczna() * 0.6)
        punkty_zycia_bohatera -= round(losowy_potwor["obrazenia potwora"] * (1 - wytrzymalosc * 0.01))
        przerwa_print("Wykonujesz silny cios mieczem!",1)
        przerwa_print(f"Wróg ma teraz {losowy_potwor['punkty zdrowia potwora']} punktów zdrowia!",1)
        przerwa_print(f"Otrzymujesz {round(losowy_potwor['obrazenia potwora'] * (1 - wytrzymalosc * 0.01))} obrażeń!",1)
        przerwa_print(f"Masz teraz {round(punkty_zycia_bohatera)} punktów zdrowia!",1)
    elif bron == "rapier":
        losowy_potwor["punkty zdrowia potwora"] -= round((obrazenia + szansza_krytyczna()) * 0.7 + atak_rapiera())
        punkty_zycia_bohatera -= round(losowy_potwor["obrazenia potwora"] * (1 - wytrzymalosc * 0.01))
        przerwa_print("Wykonujesz szybkie pchnięcia rapierem!",1)
        przerwa_print(f"Trafiasz wroga {pchniecia} razy!",1)
        przerwa_print(f"Wróg ma teraz {losowy_potwor['punkty zdrowia potwora']} punktów zdrowia!",1)
        przerwa_print(f"Otrzymujesz {round(losowy_potwor['obrazenia potwora'] * (1 - wytrzymalosc * 0.01))} obrażeń!",1)
        przerwa_print(f"Masz teraz {round(punkty_zycia_bohatera)} punktów zdrowia!",1)
    elif bron == "łuk":
        losowy_potwor["punkty zdrowia potwora"] -= round(obrazenia + szansza_krytyczna() * 1.2)
        przerwa_print("Odskakujesz przeciwnikowi na dystans dzięki czemu ciężej cię trafić!",1)
        przerwa_print("Wykonujesz celny strzał łukiem!",1)
        przerwa_print(f"Wróg ma teraz {losowy_potwor['punkty zdrowia potwora']} punktów zdrowia!",1)
        luk_odskok()

#egzekucja
#1/4 szams ma zabicie wroga w jednym ruchu, w przypadku niepowodzenia gracz otrzymuje dodatkowe obrażenia
def egzekucja():
    global wytrzymalosc
    global punkty_zycia_bohatera
    global losowy_potwor
    if random.randint(1, 4) == 1:
        losowy_potwor["punkty zdrowia potwora"] = 0
        przerwa_print("Z całych swoich sił starasz się wykończyć potwora...",1)
        przerwa_print("Udaje ci się!",1)
    else:
        punkty_zycia_bohatera -= round(losowy_potwor["obrazenia potwora"] * (1 - wytrzymalosc * 0.01)) * 1.5
        przerwa_print("Z całych swoich sił starasz się wykończyć potwora...",1)
        przerwa_print("Nie udaje ci się! Otrzymujesz dodatkowe obrażenia!",1)
        przerwa_print(f"Otrzymujesz {round(losowy_potwor['obrazenia potwora'] * (1 - wytrzymalosc * 0.01)* 1.5)} obrażeń!",1)
        przerwa_print(f"Masz teraz {round(punkty_zycia_bohatera)} punktów zdrowia!",1)

#pokoj na klucz
def pokoj_na_klucz():
    losowe_runy = random.sample(runy, 3)
    przerwa_print("W pokoju widzisz losowe runy, każda z nich daje inne statystyki.",1)
    przerwa_print("Wybierz magiczną runę:",1)

# Wyświetla listę losowych run i pozwala graczowi wybrać jedną z nich.
# Każda runa zwiększa losową statystykę bohatera szczęście, punkty życia, wytrzymałość lub obrażenia.
    for i, runa in enumerate(losowe_runy, start=1):
        print(f"{i}. {runa['runa']} {runa['moc runy']} ({runa['ulepszenie']})")

    while True:
        try:
            wybor = int(input("Podaj numer runy, którą chcesz wybrać (1-3): ")) - 1
            if 0 <= wybor < 3:
                global punkty_zycia_bohatera
                global szczescie
                global obrazenia
                global wytrzymalosc

                wybrana_runa = losowe_runy[wybor]

                if wybrana_runa['runa'] == "runa szczęścia":
                    szczescie += wybrana_runa['moc runy']
                    time.sleep(1)
                    przerwa_print(f"Masz teraz {szczescie} szczęścia.",1)
                elif wybrana_runa['runa'] == "runa vitalności":
                    punkty_zycia_bohatera += wybrana_runa['moc runy']
                    time.sleep(1)
                    przerwa_print(f"Masz teraz {round(punkty_zycia_bohatera)} punktów życia.",1)
                elif wybrana_runa['runa'] == "runa wytrzymałości":
                    wytrzymalosc += wybrana_runa['moc runy']
                    time.sleep(1)
                    przerwa_print(f"Masz teraz {wytrzymalosc} wytrzymałości.",1)
                elif wybrana_runa['runa'] == "runa siły":
                    obrazenia += wybrana_runa['moc runy']
                    time.sleep(1)
                    przerwa_print(f"Masz teraz {obrazenia} obrażeń.",1)

                break
            else:
                print("Niepoprawny wybór. Podaj numer od 1 do 3.")
        except ValueError:
            print("Niepoprawny wybór. Podaj numer od 1 do 3.")


#runy
runy = [
    {"runa": "runa szczęścia", "moc runy": random.randint(5,30), "ulepszenie": "szczęścia"},
    {"runa": "runa vitalności", "moc runy": random.randint(10,35),"ulepszenie": "punktów życia"},
    {"runa": "runa wytrzymałości", "moc runy": random.randint(5,20),"ulepszenie": "wytrzymałości"},
    {"runa": "runa siły", "moc runy": random.randint(5,30),"ulepszenie": "obrażeń"},
]

#pokój w którym jest element walki z losowym potworem
def pokoj_z_potworem():
    time.sleep(1)
    print("Podchodzisz do postaci, a to", losowy_potwor["potwor"])
    print(losowy_potwor["potwor"], "ma ", losowy_potwor["punkty zdrowia potwora"], " punktów zdrowia!")
    global dodatkowe_zycie
    global punkty_zycia_bohatera
    global liczba_kluczy
    while punkty_zycia_bohatera > 0 and losowy_potwor["punkty zdrowia potwora"] > 0:
        print("Wybierz atak:")
        print("[1] " f"Atak specjalny broni: {bron}")
        print("[2] Egzekucja")

        wybor_ataku = input().lower()

        if wybor_ataku == "1" or wybor_ataku == bron:
            rodzaj_broni()
        elif wybor_ataku == "2" or wybor_ataku == "egzekucja":
            egzekucja()
        else:
            print("Niepoprawny wybór, spróbuj jeszcze raz.")

#Wszystkie możliwości po skończeniu walki śmierć, wygrana, mechanika dodatkowego życia.
    if losowy_potwor["punkty zdrowia potwora"] <= 0 and punkty_zycia_bohatera <= 0 and dodatkowe_zycie == 0:
        time.sleep(1)
        przerwa_print("Potwór pada na ziemie...".center(szerokosc),1)
        przerwa_print("a wraz z potworem ty...".center(szerokosc),1)
        przerwa_print("Koniec. Umarłeś.".center(szerokosc),10)
        sys.exit()
    elif losowy_potwor["punkty zdrowia potwora"] <= 0 and punkty_zycia_bohatera >= 0:
        print("Pokonałeś potwora!")
        time.sleep(5)
    elif losowy_potwor["punkty zdrowia potwora"] >= 0 and punkty_zycia_bohatera <= 0 and dodatkowe_zycie == 0:
        przerwa_print("Zostałeś pokonany! Gra kończy się.",20)
        sys.exit()
    elif punkty_zycia_bohatera <= 0 and dodatkowe_zycie == 1:
        dodatkowe_zycie -= 1
        punkty_zycia_bohatera = 20
        przerwa_print("Umarłeś ".center(szerokosc),2)
        przerwa_print("ale czy ".center(szerokosc),1)
        przerwa_print("napewno? ".center(szerokosc),1)
        for linia in unikniecie_smierci:
            print(linia)
            time.sleep(2)
        time.sleep(2)
        przerwa_print("Otrzymałeś 20 punktów zdrowia!",1)
        input("Naciśnij enter aby kontynuować... \n")

    print("Przy ciele potwora znajdujesz klucz do drzwi!")
    liczba_kluczy += 1
    if liczba_kluczy == 1:
        print(f"Masz przy sobie {liczba_kluczy} klucz!")
    else:
        print(f"Masz przy sobie {liczba_kluczy} klucze!")



pokoj_z_potworem()
time.sleep(1)
przerwa_print("Znowu stajesz przed wyborem dwóch drzwi.",1)
przerwa_print("Tym razem możesz spróbować wejść do pomieszczenia zamkniętego na klucz!",1)

def wybor_pokoju():
    pokoj = 0
    powrot_punktow_zdrowia_potwora()
    global liczba_kluczy
    global losowy_potwor
    losowy_potwor = random.choice(wrogowie)
    przerwa_print("Wybierz do jakiego pomieszczenia chcesz wejść. ",1)
    print("[1] pokój z potworem")
    print("[2] pokój na klucz")
    while pokoj not in ["1", "2", "pokój z potworem", "pokój na klucz"]:

        pokoj = input().lower()
        if(pokoj == "1" or pokoj == "pokój z potworem"):
            pokoj_z_potworem()

        elif(pokoj == "2" or pokoj == "pokój na klucz"):
            if liczba_kluczy != 0:
                liczba_kluczy -= 1
                pokoj_na_klucz()
                break
            else: print("Nie masz kluczy, musisz iść do pokoju z potworem!")
            pokoj_z_potworem()
            break
        else: print("Niepoprawne dane. Spróbuj jeszcze raz! ")
time.sleep(1)
przerwa_print("Idziesz coraz dalej znowu masz do wyboru dwa pomieszczenia!",1)
wybor_pokoju()
time.sleep(1)
przerwa_print("Czujesz że zbliżasz się do brata ale przed tobą jeszcze pare pomieszczeń",1)
wybor_pokoju()
wybor_pokoju()
wybor_pokoju()
wybor_pokoju()
time.sleep(1)
przerwa_print("Słyszysz w oddali głos swojego brata, który cię woła, wiesz już tylko jeden pokój dzieli cię od uratowania go.",1)
wybor_pokoju()
time.sleep(1)
przerwa_print("Wychodzisz z pokoju i ku twoim oczom ukazuje się wielka sala tronowa, w niej widzisz swojego brata...",1)
#zakończeńie zależy od tego czy straciliśmy dodatkowe życie czy nie.
if dodatkowe_zycie == 1:
    przerwa_print("Durandal wstaję i dziękuje ci za pomoc, razem uciekacie z zamku,",2)
    przerwa_print("jednocześnie ratując również paru zabłąkanych angielskich i szwedzkich rycerzy.",2)
    przerwa_print("Duralndal ratuje Szkocję, a ty jesteś krajowym bohaterem!",2)
    przerwa_print("Dobre zakończenie!",10)
    sys.exit()
else:
    przerwa_print("Durandal leży ledwo żywy na ziemi...",2)
    przerwa_print("Z jego ust, choć ciężko zrozumieć wybrzmiewa, iż poświecił się dla ciebie...",2)
    przerwa_print("Udaje ci się opóścić przeklęty zamek...",2)
    przerwa_print("Wszyscy uważają, że doprowadziłeś do zdraty stanu wracając sam z podróży...",2)
    przerwa_print("Lud domaga się publicznej egzekucji, lecz ty uciekasz i ślad po tobie zanika.",2)
    przerwa_print("Czy dało się inaczej? Co zrobiłeś żle?",2)
    przerwa_print("Złe zakończenie!",10)
    sys.exit()