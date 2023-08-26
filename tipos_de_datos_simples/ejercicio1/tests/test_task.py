import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        resultado_esperado = "¡Hola Mundo!\n"

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Ejecutar el código que imprime
            import tipos_de_datos_simples.ejercicio1.task

            # Obtener el valor impreso capturado
            salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida coincide con la salida esperada
        self.assertEqual(salida_obtenida, resultado_esperado)


if __name__ == '__main__':
    unittest.main()
