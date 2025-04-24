drinks = {'Latte':4.20, 'Americano':2.20, 'Coffee':1.90, 'Tea':1.20, 'Espresso':1.20}
print(drinks)
drinks['Iced Tea'] = 2.40
drinks['Cappucino'] = 2.40
drinks['Hot Chocolate'] = 1.80
print(drinks)
selection = input("Enter in the drink you want to know the price of:  ")
if selection in drinks:
    print(drinks.get(selection))
else:
    print("Selection is not in the dictionary")
for books in drinks.keys():
    print(books)
for cost in drinks.values():
    print(cost)
del drinks['Latte']
drinks['Tea'] = 2
print(drinks)
