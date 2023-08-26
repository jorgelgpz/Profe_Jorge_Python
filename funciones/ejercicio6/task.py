def mean(sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve la media de los números en sample.
    """
    return sum(sample) / len(sample)


print(mean([1, 2, 3, 4, 5]))
# resultado esperado: 3.0
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
# resultado esperado: 8.700000000000001
