import unittest
from unittest.mock import patch
import sys
from io import StringIO

from programacion_funcional.ejercicio6.task import apply_grade


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = {'MATEMÁTICAS': 'NA', 'FÍSICA': 'NA', 'QUÍMICA': 'NR', 'ECONOMÍA': 'ND', 'HISTORIA': 'NE',
                           'PROGRAMACIÓN': 'NM'}

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(apply_grade(
            {'Matemáticas': 6.5, 'Física': 5, 'Química': 3.4, 'Economía': 8.2, 'Historia': 9.7, 'Programación': 10}),
            salida_esperada)

    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = {'MATEMÁTICAS': 'ND', 'FÍSICA': 'NA', 'QUÍMICA': 'NR', 'ECONOMÍA': 'NE', 'HISTORIA': 'NE',
                           'PROGRAMACIÓN': 'NM'}

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(apply_grade(
            {'Matemáticas': 8, 'Física': 5, 'Química': 2.4, 'Economía': 9.2, 'Historia': 9.7, 'Programación': 10}),
            salida_esperada)
