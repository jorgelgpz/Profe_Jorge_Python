import unittest
from unittest.mock import patch
import sys
from io import StringIO

from programacion_funcional.ejercicio3.task import filtra_lista, par


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = [2, 4, 6]

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(filtra_lista(par, [1, 2, 3, 4, 5, 6]), salida_esperada)

    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = [2, 4, 6, 8]

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(filtra_lista(par, [1, 2, 3, 4, 5, 6, 7, 8]), salida_esperada)
