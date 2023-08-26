import unittest
from unittest.mock import patch
import sys
from io import StringIO

from funciones.ejercicio8.task import statistics


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = {'media': 3.0, 'varianza': 2.0, 'desviacion tipica': 1.4142135623730951}

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(statistics([1, 2, 3, 4, 5]), resultado_esperado)

    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = {'media': 8.700000000000001, 'varianza': 18.95666666666665,
                              'desviacion tipica': 4.353925431913901}

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]), resultado_esperado)
