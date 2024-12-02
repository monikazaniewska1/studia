# PRogram przyjmuje dowolnie dluga liczbe i zwraca sume cyfr z ktorych sie sklada


while True:
    try:
        number = int(input("Podaj liczbe: "))
        break
    except:
        print("Jeszcze raz")


str_number = str(number)
sum =0

for digit in str_number:
    sum += int(digit)
print(sum)
