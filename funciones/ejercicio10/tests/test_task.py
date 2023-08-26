import unittest
from unittest.mock import patch
import sys
from io import StringIO

from funciones.ejercicio10.task import to_decimal, to_binary


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = 22

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(to_decimal('10110'), resultado_esperado)

    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = '10110'

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(to_binary(22), resultado_esperado)
