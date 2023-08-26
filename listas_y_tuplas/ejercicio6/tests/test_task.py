import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        salida_esperada = """['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'o', 'p', 'r', 's', 'u', 'v', 'x', 'y']\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Ejecutar el código que imprime y solicita la entrada
            import listas_y_tuplas.ejercicio6.task

            # Obtener la salida impresa y la entrada solicitada
            salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()
