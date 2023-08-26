import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "100.23\n"
        salida_esperada = """Introduce el precio del producto con dos decimales:100 colones y 23 céntimos.\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import cadenas.ejercicio8.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

        def test_resultado(self):
            entrada_esperada = "200.23\n"
            salida_esperada = """Introduce el precio del producto con dos decimales:200 colones y 23 céntimos.\n"""

            # Redirigir la salida estándar a un StringIO
            with patch('sys.stdout', new=StringIO()) as salida_mock:
                # Redirigir la entrada estándar a un StringIO
                with patch('sys.stdin', new=StringIO(entrada_esperada)):
                    # Ejecutar el código que imprime y solicita la entrada
                    import cadenas.ejercicio8.task

                    # Obtener la salida impresa y la entrada solicitada
                    salida_obtenida = salida_mock.getvalue()

            # Verificar si la salida obtenida y la entrada coinciden con las esperadas
            self.assertEqual(salida_obtenida, salida_esperada)


if __name__ == '__main__':
    unittest.main()
