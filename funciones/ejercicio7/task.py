def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i ** 2)
    return list


print(square([1, 2, 3, 4, 5]))
# resultado esperado: [1, 4, 9, 16, 25]
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
# resultado esperado: [5.289999999999999, 32.49, 46.239999999999995, 94.08999999999999, 146.41, 243.35999999999999]
