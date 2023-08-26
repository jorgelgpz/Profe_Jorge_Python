## Ejercicio 4

Los teléfonos de una empresa tienen el siguiente formato `prefijo-número-extension` donde 
el prefijo es el código del país `+34`, y la extensión tiene dos 
dígitos (por ejemplo `+34-913724710-56`). 
Escribir un programa que pregunte por un número de teléfono con 
este formato y muestre por pantalla el número de teléfono 
sin el prefijo y la extensión.

Debe solicitar exactamente con el siguiente texto:

`Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx:`

Y mostrar en pantalla lo siguiente, por ejemplo:

```python linenums="1"
Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx:>? +34-913724710-56
El número de teléfono es 913724710
```
**Nota:**
Usar el mensaje exacto: `El número de teléfono es <numero>` donde  `<numero>` es una variable con el resultado.