lista_zakupow = ['marchew', 'ryz', 'woda']

slownik_zakowpow = {'marchew': 3, 'ryz': 2, 'woda': 6}

print(slownik_zakowpow['marchew'])

for produkt in slownik_zakowpow:
    print(f'chcesz kupic {produkt} w ilosci {slownik_zakowpow[produkt]}')

for produkt in slownik_zakowpow.keys():
    print(f'chcesz kupic {produkt} w ilosci {slownik_zakowpow[produkt]}')

for cena in slownik_zakowpow.values():
    print(cena)

for produkt, cena in slownik_zakowpow.items(): #wszystko - klucze i wartosci
    print (f'kupujesz {produkt} po {cena} zl')