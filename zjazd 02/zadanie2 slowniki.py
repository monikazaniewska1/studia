#dany jest slownik produktow dostepnych w domu

ilość_ciast = 9999
dostpene = {'mleko': 5, 'jajka': 12, 'mąka': 4, 'masło': 2, 'woda': 10}
ciasto = {'jajka': 4, 'mąka': 0.5, 'masło': 0.6, 'mleko': 0.1}

#program liczy ile ciast mozna upiec z dostepnych skladnikow.

for składnik in ciasto:
    if dostpene[składnik] // ciasto[składnik] < ilość_ciast:
        ilość_ciast = dostpene[składnik] //ciasto[składnik]

print("Możesz wykonać", ilość_ciast, "ciast")