import unittest
from unittest.mock import patch
import sys
from io import StringIO

from funciones.ejercicio5.task import cilinder_volume


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = 141.3675

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(cilinder_volume(3,5), resultado_esperado)

    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = 301.584

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(cilinder_volume(4,6), resultado_esperado)

