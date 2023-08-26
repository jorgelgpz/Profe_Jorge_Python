import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):


    def test_resultado(self):
        entrada_esperada = "10\n10\n3\n"
        salida_esperada = """¿Cantidad a invertir?¿Interés porcentual anual?¿Años?Capital tras 1 años: 11.0\nCapital tras 2 años: 12.1\nCapital tras 3 años: 13.31\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import bucles.ejercicio4.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


    def test_resultado(self):
        entrada_esperada = "10\n10\n2\n"
        salida_esperada = """¿Cantidad a invertir?¿Interés porcentual anual?¿Años?Capital tras 1 años: 11.0\nCapital tras 2 años: 12.1\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import bucles.ejercicio4.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()
