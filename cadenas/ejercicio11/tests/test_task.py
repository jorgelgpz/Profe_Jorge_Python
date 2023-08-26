import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "pera\n50\n2\n"
        salida_esperada = """Introduce el nombre del producto:Introduce el precio unitario:Introduce el número de unidades:pera: 2 unidades x 50.00 = 100.00\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import cadenas.ejercicio11.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_resultado(self):
        entrada_esperada = "pera\n50\n3\n"
        salida_esperada = """Introduce el nombre del producto:Introduce el precio unitario:Introduce el número de unidades:pera: 3 unidades x 50.00 = 150.00\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import cadenas.ejercicio11.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()
