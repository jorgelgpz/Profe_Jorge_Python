frutas = {'Plátano': 50, 'Manzana': 60, 'Pera': 70, 'Naranja': 80}
fruta = input('¿Qué fruta quieres?').title()
kg = float(input('¿Cuántos kilos?'))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta] * kg, 'colones')
else:
    print("Lo siento, la fruta", fruta, "no está disponible.")