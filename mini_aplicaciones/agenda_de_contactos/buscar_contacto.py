def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        print("Contacto encontrado:")
        print(nombre, "-", agenda[nombre])
    else:
        print("Contacto no encontrado.")
