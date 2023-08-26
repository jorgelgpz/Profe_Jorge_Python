cantidad = float(input("¿Cantidad a invertir?"))
interes = float(input("¿Interés porcentual anual?"))
annos = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** annos, 2)))
