#program pyta o zarobki i ilosc dzieci i zwierzat.  na 3cie i kolejne dziecko
#mamy 800+ zwierzak kosztuje 300 zl. program zwraca info o dochodach na glowe.

zarobki = float(input("Powiedz ile zarabiasz?"))
ilosc_dzieci = int(input("Ile masz dzieci?"))
ilosc_zwierzat = int(input("Ile masz zwierzat?"))


if ilosc_dzieci >=3 :
    dochod = zarobki + (ilosc_dzieci-2)*800 - ilosc_zwierzat*300
else:
    dochod = zarobki - ilosc_zwierzat*300

print(f'dochod na rodzine wynosi {dochod}')