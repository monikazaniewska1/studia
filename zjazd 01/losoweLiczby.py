# program losuje liczbe 0-10. Uzytkownik zgaduje. Program pisze czy jest ok
# Czy za mala czy za duza

import random
from itertools import count

counter = 0
number = random.randint(0,10)
guessed = int(input("Zgadnij liczbe"))
while True:
    if counter > 6:
        print("Za dużo niepoprawnych prób")
    elif number < guessed:
        print("Ta liczba jest za duża")
        counter = counter + 1
        guessed = int(input("Zgadnij liczbe"))
    elif number > guessed:
        counter = counter + 1
        print("Ta liczba jest za mala")
        guessed = int(input("Zgadnij liczbe"))
    else:
        print("Brawo, to jest właśnie ta liczba!")
        break

