item = input("Podaj dane: ")

try:
    item = int(item)
    print("Wpisana dana zostala skonwertowana do INT")

except:
    try:
        item = float(item)
        print("Wpisana dana zostala skonwertowana do FLOAT")

    except:
        print("Nie udalo sie rzutowanie do INT ani Float zostaje STR")