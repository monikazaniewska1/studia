# napisz program ktory przyjmuje napis string i zwraca liczbe zamoglosek

samogloski = 'aeiouyAEIOUY'

text = str(input("Podaj tekst z którego wypiszę liczbę samogłosek"))
licznik = 0

for i in range(len(text)):
    if text[i] in samogloski:
        licznik +=1
print (f'Liczba samogłosek w tekscie wynosi {licznik}')

# program ktory przyjmuje liste i zwraca nowa liste z elemenatmi w odwroconej kolejnosci

list1 = ['kot', 'pies', 'mysz', 'koń']
list2 = []
index = len(list1) - 1
while index >= 0:
    list2.append(list1[index])
    index -= 1
print(list2)

# program pozwala wprowadzic uzytkownikow i hasla do systemu - max 5. za kazdym razem
#pyta czy wprowadzic kolejnego uzytkownika i haslo. Porhgram potwierdza poprawnosc
#hasla poprzed dwukrotne wprowadzenie hasla

users = []
passwords = []
decision = input("Czy wprowadzic kolejnego uzytkownika? t/n")
counter = 0
while decision == 't' and counter < 6:
    counter += 1
    user = input("wprowadz uzytkownika")
    password1 = input("Podaj hasło")
    password2 = input("Podaj ponownie haslo")
    if password1==password2:
        users.append(user)
        passwords.append(password)
    decision = input("Czy wprowadzic kolejnego uzytkownika? t/n")

