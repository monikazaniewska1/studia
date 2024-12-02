from rozloczenie import total_money

file = 'rozliczenie.csv'
mode = 'r'
with open (file, mode) as moje_rozliczenie:
    content = moje_rozliczenie.readlines()
    print(content)

for i in range(len(content)):
    content[i] = content[i].replace('\n', '', 1)
    content[i] = content[i].split(',')
    print(content[i])

print(content) # cala lista
print(content[4]) # jedna linia
print(content[4][2]) #jedna komorka
print(content[0][2][2:5]) #kawalek stringa

# Obliczanie sredniej wyplaty
total_money = 0
for person in content[1:]: #wezmie od 2wyrazenia bo pierwszy to str
    print(person[1])
    total_money += float(person[1])
    print(total_money)
    srednia = total_money/ len(content)-1
    print(round(srednia))

#Ile kobiet na macierzynskim
counter = 0

for person in content [1:]:
    print(person[4])
    if person[4][0].lower() == 't' and person[3] == 'k':
        counter +=1
    else:
        continue
print("jest", counter, "kobiet na macierzynskim")
