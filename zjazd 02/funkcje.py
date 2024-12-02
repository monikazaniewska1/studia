def Przywitanie (imie, wiek):
    if wiek >= 18 and imie[-1] == 'a':
        print ("Dzień dobry Szanowna Pani", imie)
    if wiek >= 18 and imie[-1] != 'a':
        print("Dzień dobry Szanowny Panie", imie)
    else:
        print("Cześć", imie)

Przywitanie('Asia', 13)
Przywitanie('Jakub', 33)


def stawkaUbezpiecza (wiek, waga, czy_pali):
    stawka_bazowa = 200
    if wiek > 50:
        stawka_bazowa += wiek
    if waga > 100:
        stawka_bazowa += waga
    if czy_pali:
        stawka_bazowa *= 2
    return stawka_bazowa

stawkaUbezpiecza(20, 60, True)

def ubezpiecznie_zwierzecia (typ, wiek):
    if typ == 'pies':
        return (100 * 1.5) + (wiek -5) * 10
    else:
        return (100 * 1.2) + (wiek -7) * 8

print(f'Zapłacisz {ubezpiecznie_zwierzecia("pies", 12)}')
