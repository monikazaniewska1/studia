

#program przyjmuje dane X pracownkow, zwraca slownik {id: slownik danych}
employees = {}
id = 0
while True:
    dane = input("Podaj dane: imię, nazwisko, wiek, mail ").split()
    employee = {'imie': dane[0], 'nazwisko' : dane[1], 'wiek': dane[2], 'email': dane[3]}
    id += 1
    employees[id] = employee

    next = input("Czy chcesz podac kolejnego pracownika? t/n")
    if next != 't':
        break

