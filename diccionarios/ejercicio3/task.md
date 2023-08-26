## Ejercicio 3

Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

| Fruta   | Precio |
|:--------|:------:|
| Plátano |   50   |
| Manzana |   60   |
| Pera    |   70   |
| Naranja |   80   |

Debe solicitar exactamente con los siguientes textos:

`¿Qué fruta quieres?`

`¿Cuántos kilos?`

y mostrar finalmente por ejemplo los siguientes textos:

`<kilos> kilos de <fruta> valen <precio> colones`

donde por ejemplo en consola podría ver se así: 

```
¿Qué fruta quieres?>? Manzana
¿Cuántos kilos?>? 2
2.0 kilos de Manzana valen 120.0 colones
```
siendo los datos de entrada: `manzana` para fruta, `2` para kilo. 
Utilice tipo de dato `float` para la variable `<kilo>`
