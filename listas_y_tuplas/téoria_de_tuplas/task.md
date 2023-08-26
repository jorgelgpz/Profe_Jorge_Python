## Tuplas

Una **tupla** es una secuencias ordenadas de objetos de distintos tipos.

Se construyen poniendo los elementos entre corchetes `(`  `)` separados por comas.

Se caracterizan por:

- Tienen orden.
- Pueden contener elementos de distintos tipos.
- Son inmutables, es decir, no pueden alterarse durante la ejecución de un programa.

Se usan habitualmente para representar colecciones de datos una determinada estructura semántica, como por ejemplo un vector o una matriz.

```python linenums="1"
# Tupla vacía
type(()) # output <class 'tuple'>
# Tupla con elementos de distintos tipos
(1, "dos", True)
# Vector
(1, 2, 3)
# Matriz
((1, 2, 3), (4, 5, 6))
```

### Creación de tuplas mediante la función `Tuple`

Otra forma de crear tuplas es mediante la función `tuple = ()`.

- `tuple = (c)` : Crea una tupla con los elementos de la secuencia o colección `c`.

Se pueden indicar los elementos separados por comas, mediante una cadena, o mediante una colección de elementos iterable.

```python linenums="1"
tuple = () # output ()
tuple = (1, 2, 3) # output (1, 2, 3)
tuple = ("Python") # output ('P', 'y', 't', 'h', 'o', 'n')
tuple = ([1, 2, 3]) # output (1, 2, 3)
```

### Operaciones con tuplas

El acceso a los elementos de una tupla se realiza del mismo modo que en las listas.
También se pueden obtener subtuplas de la misma manera que las sublistas.

Las operaciones de listas que no modifican la lista también son aplicables a las tuplas.

```python linenums="1"
a = (1, 2, 3)
a[1] # output 2
len(a) # output 3
a.index(3) # output 2
0 in a # output False
b = ((1, 2, 3), (4, 5, 6))
b[1] # output (4, 5, 6)
b[1][2] # output 6
```