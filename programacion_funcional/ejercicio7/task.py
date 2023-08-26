def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.

        Si es calificación es menor a 5 devuelve ´NR´ de nota reprobada
        Si es calificación es menor a 7 devuelve ´NA´ de nota aprobada
        Si es calificación es menor a 9 devuelve ´ND´ de nota destacada
        Si es calificación es menor a 10 devuelve ´NE´ de nota superior
        Cualquier otra calificación devuelve ´NM´ de nota maxima
    '''
    if score < 5:
        return 'NR'
    elif score < 7:
        return 'NA'
    elif score < 9:
        return 'ND'
    elif score < 10:
        return 'NE'
    else:
        return 'NM'


def passed_subject(subject):
    '''
    Función que recibe una tupla con una asignatura y su nota y devuelve True si la asignatura está aprobada o False si está suspensa.abs
    Parámetros:
        subject: Es una tupla (asignatura, nota) donde nota es un valor real entre 0 y 10.
    Devuelve: True si la nota es mayor o igual que 5 y False si no.abs
    '''
    return (subject[1] >= 5)


def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    passed = dict(filter(passed_subject, scores.items()))
    subjects = map(str.upper, passed.keys())
    grades = map(grade, passed.values())
    return dict(zip(subjects, grades))


print(apply_grade(
    {'Matemáticas': 6.5, 'Física': 5, 'Química': 3.4, 'Economía': 8.2, 'Historia': 9.7, 'Programación': 10}))
# resultado esperado {'MATEMÁTICAS': 'NA', 'FÍSICA': 'NA', 'ECONOMÍA': 'ND', 'HISTORIA': 'NE', 'PROGRAMACIÓN': 'NM'}

print(apply_grade(
    {'Matemáticas': 8, 'Física': 9, 'Química': 3.4, 'Economía': 8.2, 'Historia': 9.7, 'Programación': 9}))
# resultado esperado {'MATEMÁTICAS': 'ND', 'FÍSICA': 'NE', 'ECONOMÍA': 'ND', 'HISTORIA': 'NE', 'PROGRAMACIÓN': 'NE'}
