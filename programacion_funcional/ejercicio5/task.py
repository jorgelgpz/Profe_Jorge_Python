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


def apply_grade(scores):
    '''
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        scores: Es una lista de valores reales entre 0 y 10.
    Devuelve
        La lista de calificaciones correspondiente a las notas de scores.
    '''
    return list(map(grade, scores))


print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))
# resultado esperado ['NA', 'NA', 'NR', 'ND', 'NR', 'NE', 'NM']

print(apply_grade([6.5, 6, 3.4, 8.2, 2.1, 9.7, 9]))
# resultado esperado ['NA', 'NA', 'NR', 'ND', 'NR', 'NE', 'NE']
