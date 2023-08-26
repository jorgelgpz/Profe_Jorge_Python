persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir?')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)?')
    if continuar == "Si" or continuar == "si":
        continuar = True
    else:
        continuar = False