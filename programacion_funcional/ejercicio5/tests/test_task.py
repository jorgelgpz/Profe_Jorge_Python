import unittest
from unittest.mock import patch
import sys
from io import StringIO

from programacion_funcional.ejercicio5.task import apply_grade


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = ['NA', 'NA', 'NR', 'ND', 'NR', 'NE', 'NM']

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]), salida_esperada)

    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = ['NA', 'NA', 'NR', 'ND', 'NR', 'NE', 'NE']

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(apply_grade([6.5, 6, 3.4, 8.2, 2.1, 9.7, 9]), salida_esperada)