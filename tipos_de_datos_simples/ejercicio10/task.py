peso_payaso = 112
peso_muneca = 75
payasos = int(input("Introduce el número de payasos a enviar:"))
munecas = int(input("Introduce el número de muñecas a enviar:"))
peso_total = peso_payaso * payasos + peso_muneca * munecas
print("El peso total del paquete es " + str(peso_total))