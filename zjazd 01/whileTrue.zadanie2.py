# Program losuje liczbe calkowita 0-10
#Uzyttkownik zgaduje - program pisze czy jest za mala za duza czy ok

import random

number = random.randint(0,10)
attempt = 0
while True:
    chosen_number = int(input("Podaj liczbe"))
    if chosen_number < number:
        print("Podana liczba jest za mala, sprobuj ponownie")
        attempt += 1
        chosen_number = int(input("Podaj liczbe"))
    elif chosen_number > number:
        print("Podana liczba jest za duza, sprobuj ponownie")
        attempt += 1
        chosen_number = int(input("Podaj liczbe"))

    else:
        print("Brawo zgadles!")
        break

if attempt == 3:
    print("Probowales za wiele razy")

