import unittest
from unittest.mock import patch
import sys
from io import StringIO

from programacion_funcional.ejercicio4.task import length_words


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = {'Welcome': 7, 'to': 2, 'Pytho': 5}

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(length_words('Welcome to Pytho'), salida_esperada)

    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = {'C.T.P': 5, 'San': 3, 'Rafae': 5}

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(length_words('C.T.P San Rafae'), salida_esperada)
