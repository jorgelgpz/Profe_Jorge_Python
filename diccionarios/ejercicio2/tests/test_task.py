import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "jorge\n100\nalajuela\n12345678\n"
        salida_esperada = """¿Cómo te llamas?¿Cuántos años tienes?¿Cuál es tu dirección?¿Cuál es tu número de teléfono?jorge tiene 100 años, vive en alajuela y su número de teléfono es 12345678\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import diccionarios.ejercicio2.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()