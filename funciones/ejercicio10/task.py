def to_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.

    Por ejemplo el número binario 10101100 a decimal sería:

    0 * 2^0 = 0
    0 * 2^1 = 0
    1 * 2^2 = 4
    1 * 2^3 = 8
    0 * 2^4 = 0
    1 * 2^5 = 32
    0 * 2^6 = 0
    1 * 2^7 = 128

    Sumando los resultados de las potencias:
    0 + 0 + 4 + 8 + 0 + 32 + 0 + 128 = 172
    Por tal, el número binario 10101100es el 172 decimal.

    Nota con la función reverse() de python puede invertir la cadena
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal


def to_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.

    Por ejemplo el número decimal 23519:

    23519 / 2 = 11759 Residuo: 1
    11759 / 2 = 5879 Residuo: 1
    5879 / 2 = 2939 Residuo: 1
    2939 / 2 = 1469 Residuo: 1
    1469 / 2 = 734 Residuo: 1
    734 / 2 = 367 Residuo 0
    367 / 2 = 183 Residuo: 1
    183 / 2 = 91 Residuo: 1
    91 / 2 = 45 Residuo: 1
    45 / 2 = 22 Residuo: 1
    22/ 2 = 11  Residuo: 0
    11 / 2 = 5  Residuo: 1
    5 / 2 = 2 Residuo: 1
    2 / 2 = 1  Residuo: 0
    1 / 2 = 0  Residuo: 1

    Acomodando los residuos en orden inverso el número decimal 23519 sería el 101101111011111 binario.

    Nota con la función reverse() de python puede invertir la cadena
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)


print(to_decimal('10110'))
# resultado esperado: 12

print(to_binary(22))
# resultado esperado: 10110

print(to_decimal(to_binary(22)))
# resultado esperado: 12

print(to_binary(to_decimal('10110')))
# resultado esperado: 10110
