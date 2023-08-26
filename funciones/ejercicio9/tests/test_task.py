import unittest
from unittest.mock import patch
import sys
from io import StringIO

from funciones.ejercicio9.task import mcd, mcm


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = 12

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(mcd(24, 36), resultado_esperado)

    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = 72

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(mcm(24, 36), resultado_esperado)