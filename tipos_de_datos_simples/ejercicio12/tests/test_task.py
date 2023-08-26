import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "10\n"
        salida_esperada = "Introduce el número de barras vendidas que no son frescas:El coste de una barra fresca es ₡3.49\nEl descuento sobre una barra no fresca es 60.0%\nEl coste final a pagar es ₡13.96\n"

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import tipos_de_datos_simples.ejercicio12.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_resultado(self):
        entrada_esperada = "20\n"
        salida_esperada = "Introduce el número de barras vendidas que no son frescas:El coste de una barra fresca es ₡3.49\nEl descuento sobre una barra no fresca es 60.0%\nEl coste final a pagar es ₡27.92\n"

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import tipos_de_datos_simples.ejercicio12.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()
