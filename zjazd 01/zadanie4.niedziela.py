#program przyjmuje dowolnie dluga liczbe i zwraca sume jej cyfr.


number = int(input("Podaj liczbe"))
sum = 0

number_str = str(number)
for digit in number_str:
    sum += int(digit)

print(sum)