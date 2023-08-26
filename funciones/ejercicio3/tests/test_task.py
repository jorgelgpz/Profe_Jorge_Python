import unittest
from unittest.mock import patch
import sys
from io import StringIO

from funciones.ejercicio3.task import factorial


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test(self):
        datos_entrada = "4"  # Datos de entrada simulados
        resultado_esperado = 24

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Redirigir la entrada estándar a un StringIO
        with patch('builtins.input', side_effect=StringIO(datos_entrada)):
            factorial(datos_entrada)

            # Restaurar la salida estándar y obtener el valor impreso
            resultado = sys.stdout.getvalue()
            sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(factorial(datos_entrada), resultado_esperado)

    def test(self):
        datos_entrada = "20"  # Datos de entrada simulados
        resultado_esperado = 2432902008176640000

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Redirigir la entrada estándar a un StringIO
        with patch('builtins.input', side_effect=StringIO(datos_entrada)):
            factorial(datos_entrada)

            # Restaurar la salida estándar y obtener el valor impreso
            resultado = sys.stdout.getvalue()
            sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(factorial(datos_entrada), resultado_esperado)