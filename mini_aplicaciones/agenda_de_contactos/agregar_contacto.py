def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto agregado:", nombre, "-", telefono)