## La función enumerate()

La función incorporada (i.e. no necesita importarse) `enumerate()` toma como argumento un objeto iterable `it` y retorna 
otro cuyos elementos son tuplas de dos objetos, el primero de los cuales indica la posición de un elemento perteneciente 
a `it` y el segundo, el elemento mismo.

Para dilucidar esta un tanto oscura definición, véase el siguiente ejemplo.

```python linenums="1"
lenguajes = ["Java", "C", "C++", "Rust", "Elixir"]
list(enumerate(lenguajes))
```
`output`
```py 
[(0, 'Java'), (1, 'C'), (2, 'C++'), (3, 'Rust'), (4, 'Elixir')]
```

El resultado es un objeto iterable que contiene tuplas, dentro de las cuales el primer valor es un número correspondiente 
a la posición del lenguaje en la lista `lenguajes`, y el segundo es el nombre del lenguaje mismo.

Por defecto las posiciones empiezan desde el cero, pero puede indicarse el número de inicio como segundo argumento.

```python linenums="1"
list(enumerate(lenguajes, 1))
```
`output`
```py 
[(1, 'Java'), (2, 'C'), (3, 'C++'), (4, 'Rust'), (5, 'Elixir')]
```

La función `enumerate()` es especialmente útil cuando al emplear un bucle `for` se precisa tanto de los elementos de un 
iterable como de su posición.

```python linenums="1"
for i, lenguaje in enumerate(lenguajes):
    print(i, lenguaje)
```
`output`
```py 
0 Java
1 C
2 C++
3 Rust
4 Elixir
```

Este método es más rápido, legible y recomendable que el siguiente.

```python linenums="1"
for i in range(len(lenguajes)):
    print(i, lenguajes[i])
```
`output`
```py 
0 Java
1 C
2 C++
3 Rust
4 Elixir
```