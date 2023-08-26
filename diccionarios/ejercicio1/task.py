monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
moneda = input("Introduce una divisa:")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")