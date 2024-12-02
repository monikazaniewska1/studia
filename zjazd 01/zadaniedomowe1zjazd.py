import _random
import random

# pole prostokąta

lenghth1 = float(input("Podaj długość pierwszego boku w cm"))
length2 = float(input("Podaj długość drugiego boku w cm"))

rectangle_area = lenghth1*length2
print(f'Pole prostokąta wynosi {rectangle_area} cm')

#Sprawdzanie liczby parzystej

number = int(input("Podaj liczbę w celu sprawdzenia czy jest parzysta czy nieparzysta"))

if number%2 == 0:
    print("Liczba", number,  "jest parzysta")
else:
    print("Liczba", number, "jest nieparzysta")


#Powitanie użytkownika

name = str(input("Podaj imię"))
print("Witaj", name, "!")

# Lista ulubionych kolorow

colours = []
while True:
    colour = input("Podaj swoje ulubione kolory, jesli chcesz zakonczyc to nacisnij 'e'")
    if colour == 'e':
        break
    else:
        colours.append(colour)

print("Twoje ulubione kolory to: ", colours)

#Średnia 3 liczb

number1 = float(input("Podaj pierwszą liczbę"))
number2 = float(input("Podaj drugą liczbę"))
number3 = float(input("Podaj trzecią liczbę"))

avarage = (number1 + number2 + number3)/ 3

print (f'Średnia z podanych liczb wynosi: {avarage}')

# Konwersja temperatury
def ctoF (celcius):
    fahrenheit = celcius * 9 / 5 + 32
    print (celcius, "to jest", fahrenheit, "stopni Fahrenheita")
    return fahrenheit


def ftoC (fahrenheit):
    celcius = (fahrenheit - 32)*5 / 9
    print (fahrenheit, "stopni Fahrenheita to", celcius, "stopni Celcjusza")
    return celcius

print (ctoF(20))
print(ftoC(86))

# Wyswietlenie liczb nieparzystych

nieparzyste = []
for i in range(0, 20):
    if i % 2 != 0:
        nieparzyste.append(i)
    else:
        continue

print(nieparzyste)

# Sprawdzenie pelnoletnosci

age = int(input("Witaj użytkowniku. Podaj swoj wiek"))

if age < 18:
    print("Jesteś niepełnoletni. Do pełnoletności brakuje Ci", 18-age)
else:
    print("Jesteś dorosły")

#Prosty kalkulator
print("Wezmę od Ciebie dwie liczby i podam ich sumę, różnicę, iloczyn i iloraz")
num1 = float(input("Podaj pierwsza liczbę"))
num2 = float(input("Podaj drugą liczbę"))

sum = num1 + num2
if num1 > num2:
    sub = num1 - num2
else:
    sub = num2 - num1

multiplication = num1 *num2

if num1 > num2:
    division = num1/num2
else:
    division = num2/num1
print("Suma twoich liczb wynosi: ", sum, "różnica wynosi: ", sub, "wynik monożenia to: ", multiplication, "a dzielnenia to: ", division)

# Odwracanie ciągu znaków

string = str(input("Cześć. Podaj wyraz, a ja napiszę go w odwróconej kolejności"))

reversed_string = string[::-1]

print(reversed_string)


#kalkulator BMI

print("Witaj w kalkulatorze BMI")
weight = float(input("Podaj swoją wagę w kilogramach"))
height = float(input("Podaj swój wzrost w metrach"))

BMI = weight/ (height * height)

if BMI < 18.5:
    print("Wynik BMI wynosi: ", BMI, "Masz niedowagę")
elif 18.5 < BMI < 25:
    print("Wynik BMI wynosi: ", BMI, "Twoja waga jest prawidłowa")
else:
    print("Wynik BMI wynosi: ", BMI, "Masz nadwagę.")

# Szyfr Cezara


# text = str(input("Podaj tektst do zaszyfrowania"))
# new_text = ""
# key = 5
# for i in range(len(text)):
#    if i.islower():
#        shift = odr('a')
#    else:
#        shift = odr('A')

#Zgadnij liczbe

number = random.randrange(1, 100)
guessed_number = int(input("Zgadnij liczbę którą dla Ciebie wylosowałem"))

while True:
    if guessed_number < 0 or guessed_number > 100:
        print("Ta liczba jest spoza zakresu ")
        guessed_number = int(input("Zgadnij liczbę którą dla Ciebie wylosowałem"))
    if guessed_number == number:
        print("Brawo to jest właśnie ta liczba!")
        break
    if guessed_number > number:
        print ("Wylosowana liczba jest mniejsza")
        guessed_number = int(input("Zgadnij liczbę którą dla Ciebie wylosowałem"))
    if guessed_number < number:
        print("Wylosowana liczba jest większa")
        guessed_number = int(input("Zgadnij liczbę którą dla Ciebie wylosowałem"))

#Liczby pierwsze

liczby_pierwsze = []
n = input("Prosze podać liczbę końcową zakresu z którego mamy podać liczby pierwsze")
if n < 2:
    print("Liczba nie może być mniejsza od 2")
else:
    for number in range(2, n+1):
        pierwsza = True
        for i in range(2, int(number**0.5)+ 1):
            if number % i == 0:
                pierwsza = False
                break
            if pierwsza:
                liczby_pierwsze.append(number)
print(f"liczby pierwsze z tego zakresu to {liczby_pierwsze}")

# walidacja hasla

password = input("Prosze podać hasło")

upper = False
digit = False
for sign in password:
    if sign.isupper():
        upper = True
    if sign.isdigit():
        digit = True

if upper and digit:
    print("Hasło jest poprawne")
elif not upper:
    print("Hasło musi zawierać przynajmniej jedną wielką literę. Spróbuj ponownie")
    password = input("Prosze podać hasło")

elif not digit:
    print("Hasło musi zawierać przynajmniej jedną cyfrę. Spróbuj ponownie.")
    password = input("Prosze podać hasło")

else:
    print("Hasło musi zawierać jedną wielką literę i jedną cyfrę. Spróbuj ponownie")
    password = input("Prosze podać hasło")


#Sortowanie listy Napisz funkcję, która przyjmuje listę liczb i zwraca
# ją posortowaną w kolejności malejącej bez użycia wbudowanych funkcji sortujących.

numbers1 =[]
while True:
    number = int(input("Podaj liczbę którą chcesz wpisac do listy:"))
    numbers1.append(number)
    decision = input("Chcesz podać wiecej liczb? y/n").lower()

    if decision == 'n':
        break
numbers1.sort()
print("Lista po sortowaniu to: ", numbers1)

#Analiza tekstu Napisz program, który pobierze od użytkownika tekst i wyświetli:
# Liczbę znaków w tekście
# Liczbę słów
# Liczbę zdań (przyjmij, że zdania kończą się kropką, wykrzyknikiem lub znakiem zapytania)

text = str(input("Podaj tekst, który chcesz przeanalizować"))

print("Liczba znaków w twoim napisie to: ", len(text))

words_text = text.split()
print("Liczba słów w tekscie to: ", len(words_text))

endings = text.count('.') + text.count('!') + text.count('?')
print("Liczba zdań w tekscie to: ", endings)

# silnia

liczba = int(input("Podaj liczbę z której mam obliczyć silnię."))

