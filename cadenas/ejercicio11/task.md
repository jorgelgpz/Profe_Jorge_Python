## Ejercicio 11

Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

Debe solicitar exactamente lo siguiente texto con el orden mostrado:

`Introduce el nombre del producto:`

`Introduce el precio unitario:`

`Introduce el número de unidades:`

Luego mostrar al usuario lo siguiente:

`<producto>: <unidades> unidades x <precio> = <total>`  donde `<unidades>` es el 
número de unidades con cinco dígitos, `<precio>` es el precio unitario con 6 dígitos 
enteros y 2 decimales y <total> es el coste total con 8 dígitos enteros y 2 decimales.

En consola se ve finalmente por ejemplo:

```python linenums="1"
Introduce el nombre del producto:>? pera
Introduce el precio unitario:>? 50
Introduce el número de unidades:>? 2
pera: 2 unidades x 50.00 = 100.00
```