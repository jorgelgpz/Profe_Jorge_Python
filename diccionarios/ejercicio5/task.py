curso = {'Matemáticas': 0, 'Física': 0, 'Química': 0}
for asignatura, creditos in curso.items():

    curso[asignatura] = int(input(f'Ingrese el valor del crédito para {asignatura}'))

total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos

print('Número total de créditos del curso:', total_creditos)