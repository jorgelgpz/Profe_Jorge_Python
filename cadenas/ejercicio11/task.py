producto = input('Introduce el nombre del producto:')
precio = float(input('Introduce el precio unitario:'))
unidades = int(input('Introduce el número de unidades:'))
print(
    "{producto}: {unidades:1d} unidades x {precio:1.2f} = {total:1.2f}".format(producto=producto, unidades=unidades,
                                                                               precio=precio,
                                                                               total=unidades * precio))
