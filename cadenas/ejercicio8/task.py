precio = input("Introduce el precio del producto con dos decimales:")
print(precio[:precio.find('.')], 'colones y', precio[precio.find('.')+1:], 'céntimos.')