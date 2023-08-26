import unittest
from unittest.mock import patch
import sys
from io import StringIO

from programacion_funcional.ejercicio1.task import apply_discount, apply_IVA


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = 1349.0

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado
        suma_apply_discount = apply_discount(1000, 20) + apply_discount(500, 10) + apply_discount(100, 1)

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(suma_apply_discount, resultado_esperado)

    def test(self):
        datos_entrada = ""  # Datos de entrada simulados
        resultado_esperado = 1851.0

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Restaurar la salida estándar y obtener el valor impreso
        resultado = sys.stdout.getvalue()
        sys.stdout = stdout_guardado
        suma_apply_IVA = apply_IVA(1000, 20) + apply_IVA(500, 10) + apply_IVA(100, 1)

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(suma_apply_IVA, resultado_esperado)
