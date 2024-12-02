NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

#Iloe osob chorowalo w ostatnim roku na krzykach

print(f'\n Na krzykach chorowalo: {krzyki & chorzy_rok}'  )
print("Tych osob było: ", (len(chorzy_rok & krzyki)))

# w osttanim miesiacu w centrym
print(f'W ostatnim miesiacu chorowali: {centrum & chorzy_miesiac}')
print(' Tych osob bylo :',  len(centrum & chorzy_miesiac ))

#ile osob mieszka w sumie na krzykach i w centrum
print(f'\n Mieszkańcy w krzykach i centrym to: {centrum & krzyki}')
print('Liczba osob tam mieszkajacych to: ', len(centrum & krzyki))

#Sprawdzamy poprawnosc

print(' \n Poprawnosc danych')


#Kazdy kto chorowal w ostatnim miesiacu i roku
print(f' \n osoby które chorowały jednocześnie w tym miesiącu i roku to: {chorzy_miesiac & chorzy_rok}')
print("Ilość tych osób wynosi: ", len(chorzy_rok & chorzy_miesiac))

# Nikt nie moze mieszkac jednoczesnie w dwoch miejscach - trzeba usubac

oba = krzyki & centrum

if len(oba) != 0:
    print(' \n znaleziono duplikaty - usuwam')
    krzyki = krzyki - oba
if len(oba) == 0:
    print("Nie znaleziono duplikatow. ")

#pesele zenskie maja liczbe parzysta na koncu a meskie nieparzysta


men = set()
women = set()

for Pesel in NFZ:
    if Pesel % 2 == 0:
        women.add(Pesel)
    else:
        men.add(Pesel)
print("Męzczyźni to ", men, "a kobiety to: ", women)
