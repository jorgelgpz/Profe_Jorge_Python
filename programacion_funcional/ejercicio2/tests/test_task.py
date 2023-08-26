import unittest
from unittest.mock import patch
import sys
from io import StringIO

from programacion_funcional.ejercicio2.task import aplica_funcion_lista,cuadrado


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = [1, 4, 9, 16]

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]), salida_esperada)

    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = [1, 4, 9, 16, 25]

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(aplica_funcion_lista(cuadrado, [1, 2, 3, 4, 5]), salida_esperada)