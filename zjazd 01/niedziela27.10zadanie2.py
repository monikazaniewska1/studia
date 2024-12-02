order_list = [
    ["komputer", "patelnia"],
    ["hak", "ketchup", "sluchawki"],
    ["pierogi"],
    ["Python", "lampka", "gitara", "flet"]
]

#pogrupuj zamowienia - osobno max 2 produkty, osobno wieksze
short_order = []
long_order = []
for order in order_list:
    if len(order) <= 2:
        short_order.append(order)
    else:
        long_order.append(order)

print("Krotka lista", short_order)
print("Dluga lista", long_order)

