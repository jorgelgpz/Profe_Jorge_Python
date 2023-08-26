import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "Bruce Banner\n"
        salida_esperada = """¿Cómo te llamas?bruce banner\nBRUCE BANNER\nBruce Banner\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import cadenas.ejercicio2.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_resultado(self):
        entrada_esperada = "Tony Star\n"
        salida_esperada = """¿Cómo te llamas?tony star\nTONY STAR\nTony Star\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import cadenas.ejercicio2.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()