def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(int(n)):
        tmp *= i + 1
    return tmp


print(factorial(4))
# resultado esperado: 24

print(factorial(20))
# resultado esperado: 2432902008176640000
