my_list =[]

while True:
    product = input("Podaj produkt: ")
    my_list.append(product)
    decision = input(("Czy chcesz wprowadzic kolejny produkt? y/n"))
    if decision == 'n':
        break
print('dalsza czesc programu')
print(my_list)
