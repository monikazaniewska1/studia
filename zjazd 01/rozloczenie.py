# odczyt pliku csv zapisem poszczegolnych pol
from os.path import split

file = 'rozliczenie.csv'
mode = 'r'

with open(file, mode) as moje_rozliczenie:
    content = moje_rozliczenie.readlines()

for i in range(len(content)):
    content[i] = content[i].replace('\n', '', 1)
    content[i] = content[i].split(',')

    print(content)

print(content[4]) # jedna linia
print(content[4][2]) # jedna komorka
print(content[0][2][2:5]) # kawalek napisu

#Obliczanie sredniej wyplaty
total_money = 0
for person in content[1:]:
    print(person[1])
    total_money += float(person[1])

print("Srednia wyplata to", round(total_money/ (len(content)-1)))

# for i in range(1,len(content)):
#     print(content[i][1])
#     total_money += float(content[i][1])

#Ile kobiet na macierzynskim
counter_maternity = 0

for person in content[1:]:
   # print(person[4])
    if person[4][0].lower() == 't' and person[3] == 'k':
        counter_maternity += 1
print("jest", counter_maternity, "kobiet na macierzynskim")