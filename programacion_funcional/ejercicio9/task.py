from functools import reduce


# Función para sumar dos números
def suma(a, b):
    return a + b


# Usando reduce para sumar todos los elementos de la lista
def usando_reduce(numeros):
    return reduce(suma, numeros)


print(usando_reduce([1, 2, 3, 4, 5]))
# resultado esperado 15

print(usando_reduce([2, 3, 4, 5, 6]))
# resultado esperado 20
