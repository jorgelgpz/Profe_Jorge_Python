import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "En un lugar de la Mancha\n"
        salida_esperada = """Introduce una palabra:La vocal a aparece 4 veces\nLa vocal e aparece 1 veces\nLa vocal i aparece 0 veces\nLa vocal o aparece 0 veces\nLa vocal u aparece 2 veces\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import listas_y_tuplas.ejercicio8.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_resultado(self):
        entrada_esperada = "si funciona\n"
        salida_esperada = """Introduce una palabra:La vocal a aparece 1 veces\nLa vocal e aparece 0 veces\nLa vocal i aparece 2 veces\nLa vocal o aparece 1 veces\nLa vocal u aparece 1 veces\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import listas_y_tuplas.ejercicio8.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()
