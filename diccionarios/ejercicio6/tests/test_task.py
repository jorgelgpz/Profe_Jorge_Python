import unittest
from unittest.mock import patch
from io import StringIO


class PruebaOperaciones(unittest.TestCase):
    def test_resultado(self):
        entrada_esperada = "nombre\njorge\nsi\napellido\nperez\nno\n"
        salida_esperada = """¿Qué dato quieres introducir?nombre: {'nombre': 'jorge'}\n¿Quieres añadir más información (Si/No)?¿Qué dato quieres introducir?apellido: {'nombre': 'jorge', 'apellido': 'perez'}\n¿Quieres añadir más información (Si/No)?"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import diccionarios.ejercicio6.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_resultado(self):
        entrada_esperada = "nombre\nluis\nsi\napellido\nperez\nno\n"
        salida_esperada = """¿Qué dato quieres introducir?nombre: {'nombre': 'luis'}\n¿Quieres añadir más información (Si/No)?¿Qué dato quieres introducir?apellido: {'nombre': 'luis', 'apellido': 'perez'}\n¿Quieres añadir más información (Si/No)?"""

        # Redirigir la salida estándar a un StringIO
        with patch('sys.stdout', new=StringIO()) as salida_mock:
            # Redirigir la entrada estándar a un StringIO
            with patch('sys.stdin', new=StringIO(entrada_esperada)):
                # Ejecutar el código que imprime y solicita la entrada
                import diccionarios.ejercicio6.task

                # Obtener la salida impresa y la entrada solicitada
                salida_obtenida = salida_mock.getvalue()

        # Verificar si la salida obtenida y la entrada coinciden con las esperadas
        self.assertEqual(salida_obtenida, salida_esperada)



if __name__ == '__main__':
    unittest.main()
