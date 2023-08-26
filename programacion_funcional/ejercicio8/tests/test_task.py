import unittest
from unittest.mock import patch
import sys
from io import StringIO

from programacion_funcional.ejercicio8.task import busca_piso


class PruebaOperaciones(unittest.TestCase):
    pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
             {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
             {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
             {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
             {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = [
            {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A', 'precio': 84000.0},
            {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A', 'precio': 95000.0}]

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(busca_piso(self.pisos, 100000),
                         salida_esperada)

    def test_resultado(self):
        entrada_esperada = ""
        salida_esperada = [
            {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A', 'precio': 104000.0},
            {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B', 'precio': 117300.0},
            {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A', 'precio': 84000.0},
            {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'precio': 133875.0},
            {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A', 'precio': 95000.0}]

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(busca_piso(self.pisos, 900000),
                         salida_esperada)
