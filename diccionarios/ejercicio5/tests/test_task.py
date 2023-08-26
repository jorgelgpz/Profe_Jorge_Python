import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "6\n4\n5\n"
        salida_esperada = """Ingrese el valor del crédito para MatemáticasIngrese el valor del crédito para FísicaIngrese el valor del crédito para QuímicaMatemáticas tiene 6 créditos\nFísica tiene 4 créditos\nQuímica tiene 5 créditos\nNúmero total de créditos del curso: 15\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import diccionarios.ejercicio5.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_resultado(self):
        entrada_esperada = "1\n2\n3\n"
        salida_esperada = """Ingrese el valor del crédito para MatemáticasIngrese el valor del crédito para FísicaIngrese el valor del crédito para QuímicaMatemáticas tiene 1 créditos\nFísica tiene 2 créditos\nQuímica tiene 3 créditos\nNúmero total de créditos del curso: 6\n"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import diccionarios.ejercicio5.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

if __name__ == '__main__':
    unittest.main()
