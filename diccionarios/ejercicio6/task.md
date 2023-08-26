## Ejercicio 6

Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

Debe solicitar exactamente con el siguiente texto:

`¿Qué dato quieres introducir?`

y también si quiere continuar agregando claves al diccionario de esta manera:

`¿Quieres añadir más información (Si/No)?`

y mostrar finalmente lo siguiente, por ejemplo:

`{'nombre': 'jorge', 'apellido': 'perez'}`

siendo 'nombre' y 'apellido' las claves y 'jorge' y 'perez' los valores

En consola debe ver se el programa corriendo de la siguiente manera:

```
¿Qué dato quieres introducir?>? nombre
nombre: >? jorge
{'nombre': 'jorge'}
¿Quieres añadir más información (Si/No)?>? si
¿Qué dato quieres introducir?>? apellido
apellido: >? perez
{'nombre': 'jorge', 'apellido': 'perez'}
¿Quieres añadir más información (Si/No)?
```

Debe mostrar el diccionario cada vez que se agrega un dato como en el ejemplo

Nota: Recueda para para construir un diccionario se debe cumplir este formato: {'clave': 'valor'}, ojo al espaciado de los `: ` 