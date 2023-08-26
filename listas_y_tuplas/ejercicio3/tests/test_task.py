import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):

    def test_resultado(self):
        entrada_esperada = "6\n7\n4\n6\n5\n"
        salida_esperada = """¿Qué nota has sacado en Matemáticas?¿Qué nota has sacado en Física?¿Qué nota has sacado en Química?¿Qué nota has sacado en Historia?¿Qué nota has sacado en Lengua?En Matemáticas has sacado 6\nEn Física has sacado 7\nEn Química has sacado 4\nEn Historia has sacado 6\nEn Lengua has sacado 5\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import listas_y_tuplas.ejercicio3.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_resultado(self):
        entrada_esperada = "1\n7\n4\n6\n5\n"
        salida_esperada = """¿Qué nota has sacado en Matemáticas?¿Qué nota has sacado en Física?¿Qué nota has sacado en Química?¿Qué nota has sacado en Historia?¿Qué nota has sacado en Lengua?En Matemáticas has sacado 1\nEn Física has sacado 7\nEn Química has sacado 4\nEn Historia has sacado 6\nEn Lengua has sacado 5\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import listas_y_tuplas.ejercicio3.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()

