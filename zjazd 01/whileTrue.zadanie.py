#program przyjmuje inty tylko od 0 do 10


attempts_number = 0

while True:
    number = int(input("Podaj liczbe: "))

    if 0 < number <= 10:
        break
    attempts_number += 1

    if attempts_number == 5:
        print("Probowales za wiele razy")
        break