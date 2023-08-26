import unittest
from unittest.mock import patch
import sys
from io import StringIO

from funciones.ejercicio2.task import greet


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test(self):
        datos_entrada = "Jorge"  # Datos de entrada simulados
        resultado_esperado = "¡Hola Jorge!"

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Redirigir la entrada estándar a un StringIO
        with patch('builtins.input', side_effect=StringIO(datos_entrada)):
            greet(datos_entrada)

            # Restaurar la salida estándar y obtener el valor impreso
            resultado = sys.stdout.getvalue()
            sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(resultado.strip(), resultado_esperado)

    def test(self):
        datos_entrada = "Luis"  # Datos de entrada simulados
        resultado_esperado = "¡Hola Luis!"

        # Redirigir la salida estándar a un StringIO
        stdout_guardado = sys.stdout
        sys.stdout = StringIO()

        # Redirigir la entrada estándar a un StringIO
        with patch('builtins.input', side_effect=StringIO(datos_entrada)):
            greet(datos_entrada)

            # Restaurar la salida estándar y obtener el valor impreso
            resultado = sys.stdout.getvalue()
            sys.stdout = stdout_guardado

        # Verificar si el resultado coincide con el resultado esperado
        self.assertEqual(greet(datos_entrada), resultado_esperado)
