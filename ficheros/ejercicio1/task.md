## Ejercicio 1

Escribir una función que pida un número entero entre 1 y 10, lea el fichero `tabla-n.txt` con la tabla de multiplicar de ese número, done `n` es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello y proceder a crear un fichero con el nombre `tabla-n.txt` y la tabla de multiplicar de ese número, done `n` es el número introducido.

Por ejemlo: 

`Introduce un número entero entre 1 y 10:  4`

sí existe el fichero se lee y se muestra.

```
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
```
sino, entonces muestra el mensaje `No existe el fichero con la tabla del 4` y procede a crea el fichero `tabla-n.txt`

Nota: Utilice `try` para manejar los errores.

Al terminar llame a su profesor para revisar el código.